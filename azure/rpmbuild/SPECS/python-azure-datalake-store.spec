# Created by pyp2rpm-3.3.2
%global pypi_name azure-datalake-store

Name:           python-%{pypi_name}
Version:        0.0.48
Release:        1%{?dist}
Summary:        Azure Data Lake Store Filesystem Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-data-lake-store-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Microsoft Azure Data Lake Store Filesystem Library for Python This project is
the Python filesystem library for Azure Data Lake Store.INSTALLATION To install
from source instead of pip (for local testing and development):

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(adal) >= 0.4.2
Requires:       python2dist(azure-nspkg)
Requires:       python2dist(cffi)
Requires:       python2dist(futures)
Requires:       python2dist(pathlib2)
Requires:       python2dist(requests) >= 2.20.0
%description -n python2-%{pypi_name}
Microsoft Azure Data Lake Store Filesystem Library for Python This project is
the Python filesystem library for Azure Data Lake Store.INSTALLATION To install
from source instead of pip (for local testing and development):

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(adal) >= 0.4.2
Requires:       python3dist(azure-nspkg)
Requires:       python3dist(cffi)
Requires:       python3dist(futures)
Requires:       python3dist(pathlib2)
Requires:       python3dist(requests) >= 2.20.0
%description -n python3-%{pypi_name}
Microsoft Azure Data Lake Store Filesystem Library for Python This project is
the Python filesystem library for Azure Data Lake Store.INSTALLATION To install
from source instead of pip (for local testing and development):


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
%py3_install

%files -n python2-%{pypi_name}
%doc README.rst
%{python2_sitelib}/azure
%{python2_sitelib}/samples
%{python2_sitelib}/azure_datalake_store-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/azure
%{python3_sitelib}/samples
%{python3_sitelib}/azure_datalake_store-%{version}-py?.?.egg-info

%changelog
* Tue Feb 25 2020 mockbuilder - 0.0.48-1
- Initial package.