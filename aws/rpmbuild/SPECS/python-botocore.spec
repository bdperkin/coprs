# Created by pyp2rpm-3.3.2
%global pypi_name botocore

Name:           python-%{pypi_name}
Version:        1.15.7
Release:        1%{?dist}
Summary:        Low-level, data-driven core of boto 3

License:        Apache License 2.0
URL:            https://github.com/boto/botocore
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(docutils) < 0.16
BuildRequires:  python2dist(docutils) >= 0.10
BuildRequires:  python2dist(jmespath) < 1.0.0
BuildRequires:  python2dist(jmespath) >= 0.7.1
BuildRequires:  python2dist(python-dateutil) < 3.0.0
BuildRequires:  python2dist(python-dateutil) >= 2.1
BuildRequires:  python2dist(setuptools)
BuildRequires:  python2dist(urllib3) < 1.26
BuildRequires:  python2dist(urllib3) >= 1.20
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils) < 0.16
BuildRequires:  python3dist(docutils) >= 0.10
BuildRequires:  python3dist(jmespath) < 1.0.0
BuildRequires:  python3dist(jmespath) >= 0.7.1
BuildRequires:  python3dist(python-dateutil) < 3.0.0
BuildRequires:  python3dist(python-dateutil) >= 2.1
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(urllib3) < 1.26
BuildRequires:  python3dist(urllib3) >= 1.20
BuildRequires:  python3dist(sphinx)

%description
 A low-level interface to a growing number of Amazon Web Services. The botocore
package is the foundation for the AWS CLI < as well as boto3 < 10/09/2019
support for Python 2.6 and Python 3.3 was deprecated and support was dropped on
01/10/2020. To avoid disruption, customers using Botocore

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(docutils) < 0.16
Requires:       python2dist(docutils) >= 0.10
Requires:       python2dist(jmespath) < 1.0.0
Requires:       python2dist(jmespath) >= 0.7.1
Requires:       python2dist(python-dateutil) < 3.0.0
Requires:       python2dist(python-dateutil) >= 2.1
Requires:       python2dist(urllib3) < 1.26
Requires:       python2dist(urllib3) >= 1.20
%description -n python2-%{pypi_name}
 A low-level interface to a growing number of Amazon Web Services. The botocore
package is the foundation for the AWS CLI < as well as boto3 < 10/09/2019
support for Python 2.6 and Python 3.3 was deprecated and support was dropped on
01/10/2020. To avoid disruption, customers using Botocore

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(docutils) < 0.16
Requires:       python3dist(docutils) >= 0.10
Requires:       python3dist(jmespath) < 1.0.0
Requires:       python3dist(jmespath) >= 0.7.1
Requires:       python3dist(python-dateutil) < 3.0.0
Requires:       python3dist(python-dateutil) >= 2.1
Requires:       python3dist(urllib3) < 1.26
Requires:       python3dist(urllib3) >= 1.20
%description -n python3-%{pypi_name}
 A low-level interface to a growing number of Amazon Web Services. The botocore
package is the foundation for the AWS CLI < as well as boto3 < 10/09/2019
support for Python 2.6 and Python 3.3 was deprecated and support was dropped on
01/10/2020. To avoid disruption, customers using Botocore

%package -n python-%{pypi_name}-doc
Summary:        botocore documentation
%description -n python-%{pypi_name}-doc
Documentation for botocore

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.rst tests/unit/response_parsing/README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst tests/unit/response_parsing/README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
* Wed Feb 26 2020 mockbuilder - 1.15.7-1
- Initial package.