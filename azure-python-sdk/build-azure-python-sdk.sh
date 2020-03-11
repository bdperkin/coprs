#! /bin/bash

export http_proxy=http://localhost:3128
export https_proxy=http://localhost:3128

if [ ! -d ../../azure-sdk-for-python ]; then
    pushd ../..
    git clone https://github.com/Azure/azure-sdk-for-python.git
    if [ $? -ne 0 ]; then
        exit 1
    fi
    popd
fi

pushd ../../azure-sdk-for-python

git fetch
if [ $? -ne 0 ]; then
    exit 1
fi

git pull
if [ $? -ne 0 ]; then
    exit 1
fi

python3 setup.py clean
if [ $? -ne 0 ]; then
    exit 1
fi

python3 setup.py bdist_rpm --spec-only
if [ $? -ne 0 ]; then
    exit 1
fi

popd

rm -vrf rpmbuild
if [ $? -ne 0 ]; then
    exit 1
fi

mkdir -v -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
if [ $? -ne 0 ]; then
    exit 1
fi

mock -r fedora-31-local-x86_64 --clean
if [ $? -ne 0 ]; then
    exit 1
fi

mock -r fedora-31-local-x86_64 --init
if [ $? -ne 0 ]; then
    exit 1
fi

build_srpm() {
    SPEC=$1

    NAME=${SPEC}
    VERSION="="

    if [ -f ${SPEC} ]; then
        NAME=$(grep '%define name ' ${SPEC} | awk '{print $3}')
        VERSION=$(grep '%define version ' ${SPEC} | awk '{print $3}')
    fi

    pip3 --proxy ${http_proxy} install ${NAME}== 2>&1 | grep "ERROR: Could not find a version that satisfies the requirement ${NAME}==" | cut -d\( -f2 | cut -d\) -f1 | cut -d: -f2 | tr ',' '\n' | awk '{print $1}' | grep "^${VERSION}$"
    if [ $? -ne 0 ]; then
        VERSION=$(pip3 --proxy ${http_proxy} install ${NAME}== 2>&1 | grep "ERROR: Could not find a version that satisfies the requirement ${NAME}==" | cut -d\( -f2 | cut -d\) -f1 | cut -d: -f2 | tr ',' '\n' | awk '{print $1}' | tail -1)
    fi

    PYP2RPMCMD="pyp2rpm --proxy ${http_proxy} -b 3 -p 3 -s -d ${PWD}/rpmbuild/SOURCES -v ${VERSION} ${NAME}"
    echo Running: ${PYP2RPMCMD}
    ${PYP2RPMCMD}
    if [ $? -ne 0 ]; then
        exit 1
    fi

    mv -v rpmbuild/SOURCES/python-${NAME}.spec rpmbuild/SPECS/python-${NAME}.spec
    if [ $? -ne 0 ]; then
        exit 1
    fi

    sed -i -e "s/ ~= / >= /g" rpmbuild/SPECS/python-${NAME}.spec
    sed -i -e "s/\.\*$//g" rpmbuild/SPECS/python-${NAME}.spec
    sed -i -e "/ python3dist(enum34)/d" rpmbuild/SPECS/python-${NAME}.spec
    sed -i -e "/ python3dist(futures)/d" rpmbuild/SPECS/python-${NAME}.spec
    sed -i -e "s/^Summary:        $/Summary:        %{pypi_name}/g" rpmbuild/SPECS/python-${NAME}.spec
    sed -i -e "s/^%{?python_provide:%python_provide python3-%{pypi_name}}$/%{?python_provide:%python_provide python3-%{pypi_name}}\nProvides:       python3dist(%{pypi_name}) = %{version}/g" rpmbuild/SPECS/python-${NAME}.spec
    sed -i -e "s/^%autosetup -n %{pypi_name}-%{version}$/%autosetup -n %{pypi_name}-%{version}\n# Fix compatible release specifiers\nsed -i -e 's\/~=\/>=\/g' setup.py/g" rpmbuild/SPECS/python-${NAME}.spec
    sed -i -e "s/^%{__python3} setup.py test$/%{__python3} setup.py test || true/g" rpmbuild/SPECS/python-${NAME}.spec
    ./fix-changelog.sh rpmbuild/SPECS/python-${NAME}.spec

    rpmlint -i rpmbuild/SPECS/python-${NAME}.spec
    if [ $? -ne 0 ]; then
        exit 1
    fi

    mock -r fedora-31-local-x86_64 --buildsrpm --spec rpmbuild/SPECS/python-${NAME}.spec --sources rpmbuild/SOURCES --symlink-dereference
    if [ $? -ne 0 ]; then
        exit 1
    fi

    mv -v /var/lib/mock/*/result/python-${NAME}-*.src.rpm rpmbuild/SRPMS
    if [ $? -ne 0 ]; then
        exit 1
    fi

    REQUIRES=$(rpm -qp --requires rpmbuild/SRPMS/python-${NAME}-*.src.rpm | grep -P "^python3dist(.*)" | sort | uniq | sed -e 's/\ /~/g')
    for REQ in ${REQUIRES}; do
        REQ=$(echo ${REQ} | sed -e 's/~/\ /g')
        mock -r fedora-31-local-x86_64 --dnf-cmd provides "${REQ}"
        if [ $? -ne 0 ]; then
            PYPKG=$(echo "${REQ}" | cut -d\( -f2 | cut -d\) -f1)
            if [ ! -f rpmbuild/SPECS/python-${PYPKG}.spec ]; then
                build_srpm ${PYPKG}
            fi
        fi
    done
}

for SPEC in $(ls -trd $(find ../../azure-sdk-for-python -type f -name '*.spec' -a \! -name 'azure-core-tracing-*.spec' -a \! -name 'azure-template.spec' -print)); do
    build_srpm ${SPEC}
done

mock -r fedora-31-local-x86_64 --chain --recurse $(ls -trd rpmbuild/SRPMS/python-*-*.src.rpm)
if [ $? -ne 0 ]; then
    exit 1
fi

ls -trd /var/tmp/mock-chain-bperkins-* | tail -1 | xargs -i find {} -type f -name '*.src.rpm' -print | xargs -i mv -v -f {} rpmbuild/SRPMS
if [ $? -ne 0 ]; then
    exit 1
fi

ls -trd /var/tmp/mock-chain-bperkins-* | tail -1 | xargs -i find {} -type f -name '*.rpm' -print | xargs -i mv -v -f {} rpmbuild/RPMS
if [ $? -ne 0 ]; then
    exit 1
fi
