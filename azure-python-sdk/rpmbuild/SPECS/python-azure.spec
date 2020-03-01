# Created by pyp2rpm-3.3.2
%global pypi_name azure

Name:           python-%{pypi_name}
Version:        4.0.0
Release:        1%{?dist}
Summary:        Microsoft Azure Client Libraries for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Microsoft Azure SDK for Python This is the Microsoft Azure bundle.This package
does not contain any code in itself. It installs a set of packages that provide
Microsoft Azure functionality.All packages in this bundle have been tested with
Python 2.7, 3.4, 3.5, 3.6 and 3.7This package uses PEP440 syntax, and thus
requires pip > 6.0 and/or setuptools > 8.0 to be installed. Documentation
All...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-applicationinsights) >= 0.1.0
Requires:       python3dist(azure-batch) >= 4.1
Requires:       python3dist(azure-cosmosdb-table) >= 1.0
Requires:       python3dist(azure-datalake-store) >= 0.0.18
Requires:       python3dist(azure-eventgrid) >= 1.1
Requires:       python3dist(azure-graphrbac) >= 0.40.0
Requires:       python3dist(azure-keyvault) >= 1.0
Requires:       python3dist(azure-loganalytics) >= 0.1.0
Requires:       python3dist(azure-mgmt) >= 4.0
Requires:       python3dist(azure-servicebus) >= 0.21.1
Requires:       python3dist(azure-servicefabric) >= 6.3.0.0
Requires:       python3dist(azure-servicemanagement-legacy) >= 0.20.6
Requires:       python3dist(azure-storage-blob) >= 1.3
Requires:       python3dist(azure-storage-file) >= 1.3
Requires:       python3dist(azure-storage-queue) >= 1.3
%description -n python3-%{pypi_name}
Microsoft Azure SDK for Python This is the Microsoft Azure bundle.This package
does not contain any code in itself. It installs a set of packages that provide
Microsoft Azure functionality.All packages in this bundle have been tested with
Python 2.7, 3.4, 3.5, 3.6 and 3.7This package uses PEP440 syntax, and thus
requires pip > 6.0 and/or setuptools > 8.0 to be installed. Documentation
All...


%prep
%autosetup -n %{pypi_name}-%{version}
# Fix compatible release specifiers
sed -i -e 's/~=/>=/g' setup.py
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 4.0.0-1
- Initial package.