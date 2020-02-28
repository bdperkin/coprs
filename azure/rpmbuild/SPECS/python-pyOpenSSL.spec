# Created by pyp2rpm-3.3.2
%global pypi_name pyOpenSSL

Name:           python-%{pypi_name}
Version:        19.1.0
Release:        1%{?dist}
Summary:        Python wrapper module around the OpenSSL library

License:        Apache License, Version 2.0
URL:            https://pyopenssl.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(cryptography) >= 2.8
BuildRequires:  python3dist(flaky)
BuildRequires:  python3dist(pretend)
BuildRequires:  python3dist(pytest) >= 3.0.1
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.5.2
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx)

%description
 pyOpenSSL -- A Python wrapper around the OpenSSL library **Note:** The Python
Cryptographic Authority **strongly suggests** the use of pyca/cryptography_

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(cryptography) >= 2.8
Requires:       python3dist(flaky)
Requires:       python3dist(pretend)
Requires:       python3dist(pytest) >= 3.0.1
Requires:       python3dist(six) >= 1.5.2
Requires:       python3dist(sphinx)
Requires:       python3dist(sphinx-rtd-theme)
%description -n python3-%{pypi_name}
 pyOpenSSL -- A Python wrapper around the OpenSSL library **Note:** The Python
Cryptographic Authority **strongly suggests** the use of pyca/cryptography_

%package -n python-%{pypi_name}-doc
Summary:        pyOpenSSL documentation
%description -n python-%{pypi_name}-doc
Documentation for pyOpenSSL

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 doc html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/OpenSSL
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Feb 25 2020 mockbuilder - 19.1.0-1
- Initial package.