# Created by pyp2rpm-3.3.2
%global pypi_name azure-multiapi-storage

Name:           python-%{pypi_name}
Version:        0.2.4
Release:        1%{?dist}
Summary:        Microsoft Azure Storage Client Library for Python with multi API version support

License:        MIT
URL:            https://github.com/Azure/azure-multiapi-storage-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Microsoft Azure Storage Client Library for Python - with Multi API version
Support Handles multi-API versions of Azure Storage Data Plane originally from
This is not an official Azure Storage SDK.- It is used by to support multiple
API versions.- The official Azure Storage SDK is at The official Azure CosmosDB
Table SDK is at

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(azure-common)
Requires:       python2dist(azure-nspkg)
Requires:       python2dist(cryptography)
Requires:       python2dist(futures)
Requires:       python2dist(python-dateutil)
Requires:       python2dist(requests)
%description -n python2-%{pypi_name}
Microsoft Azure Storage Client Library for Python - with Multi API version
Support Handles multi-API versions of Azure Storage Data Plane originally from
This is not an official Azure Storage SDK.- It is used by to support multiple
API versions.- The official Azure Storage SDK is at The official Azure CosmosDB
Table SDK is at

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(azure-common)
Requires:       python3dist(azure-nspkg)
Requires:       python3dist(cryptography)
Requires:       python3dist(futures)
Requires:       python3dist(python-dateutil)
Requires:       python3dist(requests)
%description -n python3-%{pypi_name}
Microsoft Azure Storage Client Library for Python - with Multi API version
Support Handles multi-API versions of Azure Storage Data Plane originally from
This is not an official Azure Storage SDK.- It is used by to support multiple
API versions.- The official Azure Storage SDK is at The official Azure CosmosDB
Table SDK is at


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
%{python2_sitelib}/azure_multiapi_storage-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/azure
%{python3_sitelib}/azure_multiapi_storage-%{version}-py?.?.egg-info

%changelog
* Tue Feb 25 2020 mockbuilder - 0.2.4-1
- Initial package.