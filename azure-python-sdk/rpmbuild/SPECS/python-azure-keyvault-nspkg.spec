# Created by pyp2rpm-3.3.2
%global pypi_name azure-keyvault-nspkg

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        2%{?dist}
Summary:        Microsoft Azure Key Vault Namespace Package [Internal]

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Microsoft Azure SDK for PythonThis is the Microsoft Azure Key Vault namespace
package. It isn't intended to be installed directly. Key Vault client libraries
are located elsewhere: - [azure-keyvault-certificates]( - [azure-keyvault-
keys]( - [azure-keyvault-secrets]( package is for Python 2 only. It provides
the necessary files for other packages to extend the azure namespace. Python
3.x...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-nspkg) >= 3.0.0
%description -n python3-%{pypi_name}
 Microsoft Azure SDK for PythonThis is the Microsoft Azure Key Vault namespace
package. It isn't intended to be installed directly. Key Vault client libraries
are located elsewhere: - [azure-keyvault-certificates]( - [azure-keyvault-
keys]( - [azure-keyvault-secrets]( package is for Python 2 only. It provides
the necessary files for other packages to extend the azure namespace. Python
3.x...


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
%doc README.md
%{python3_sitelib}/azure
%{python3_sitelib}/azure_keyvault_nspkg-%{version}-py?.?.egg-info

%changelog
* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 1.0.0-2
- Rebuilt.

* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 1.0.0-1
- Initial package.