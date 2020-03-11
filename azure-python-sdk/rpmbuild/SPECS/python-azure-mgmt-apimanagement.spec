# Created by pyp2rpm-3.3.2
%global pypi_name azure-mgmt-apimanagement

Name:           python-%{pypi_name}
Version:        0.1.0
Release:        2%{?dist}
Summary:        Microsoft Azure API Management Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Microsoft Azure SDK for Python This is the Microsoft Azure API Management
Client Library.Azure Resource Manager (ARM) is the next generation of
management APIs that replace the old Azure Service Management (ASM).This
package has been tested with Python 2.7, 3.4, 3.5, 3.6 and 3.7.For the older
Azure Service Management (ASM) libraries, see azure-servicemanagement-legacy <
library.For a more...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-common) >= 1.1
Requires:       python3dist(azure-mgmt-nspkg)
Requires:       python3dist(msrest) >= 0.5.0
Requires:       python3dist(msrestazure) < 2.0.0
Requires:       python3dist(msrestazure) >= 0.4.32
%description -n python3-%{pypi_name}
Microsoft Azure SDK for Python This is the Microsoft Azure API Management
Client Library.Azure Resource Manager (ARM) is the next generation of
management APIs that replace the old Azure Service Management (ASM).This
package has been tested with Python 2.7, 3.4, 3.5, 3.6 and 3.7.For the older
Azure Service Management (ASM) libraries, see azure-servicemanagement-legacy <
library.For a more...


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
%{python3_sitelib}/azure
%{python3_sitelib}/azure_mgmt_apimanagement-%{version}-py?.?.egg-info

%changelog
* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 0.1.0-2
- Rebuilt.

* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 0.1.0-1
- Initial package.