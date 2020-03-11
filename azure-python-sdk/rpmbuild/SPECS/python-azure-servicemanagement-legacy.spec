# Created by pyp2rpm-3.3.2
%global pypi_name azure-servicemanagement-legacy

Name:           python-%{pypi_name}
Version:        0.20.6
Release:        2%{?dist}
Summary:        Microsoft Azure Legacy Service Management Client Library for Python

License:        Apache License 2.0
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Microsoft Azure SDK for Python This is the Microsoft Azure Service Management
Legacy Client Library.All packages in this bundle have been tested with Python
2.7, 3.3, 3.4 and 3.5.For the newer Azure Resource Management (ARM) libraries,
see azure-mgmt < a more complete set of Azure libraries, see the azure < bundle
package. Compatibility **IMPORTANT**: If you have an earlier version of the...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-common) >= 1.1.5
Requires:       python3dist(pyopenssl)
Requires:       python3dist(requests)
%description -n python3-%{pypi_name}
Microsoft Azure SDK for Python This is the Microsoft Azure Service Management
Legacy Client Library.All packages in this bundle have been tested with Python
2.7, 3.3, 3.4 and 3.5.For the newer Azure Resource Management (ARM) libraries,
see azure-mgmt < a more complete set of Azure libraries, see the azure < bundle
package. Compatibility **IMPORTANT**: If you have an earlier version of the...


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
%{python3_sitelib}/azure_servicemanagement_legacy-%{version}-py?.?.egg-info

%changelog
* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 0.20.6-2
- Rebuilt.

* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 0.20.6-1
- Initial package.