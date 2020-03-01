# Created by pyp2rpm-3.3.2
%global pypi_name azure-keyvault

Name:           python-%{pypi_name}
Version:        4.0.0
Release:        1%{?dist}
Summary:        Microsoft Azure Key Vault Client Libraries for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Azure Key Vault client libraries for PythonThis is the Microsoft Azure Key
Vault libraries bundle.This package does not contain any code in itself. It
installs a set of packages that provide APIs for Key Vault operations:- [azure-
keyvault-keys v4.0.x]( - [azure-keyvault-secrets v4.0.x]( - [azure-keyvault-
certificates v4.0.x]( Install the package Install the Azure Key Vault client
libraries...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-keyvault-keys) >= 4.0
Requires:       python3dist(azure-keyvault-secrets) >= 4.0
%description -n python3-%{pypi_name}
 Azure Key Vault client libraries for PythonThis is the Microsoft Azure Key
Vault libraries bundle.This package does not contain any code in itself. It
installs a set of packages that provide APIs for Key Vault operations:- [azure-
keyvault-keys v4.0.x]( - [azure-keyvault-secrets v4.0.x]( - [azure-keyvault-
certificates v4.0.x]( Install the package Install the Azure Key Vault client
libraries...


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
%{python3_sitelib}/azure_keyvault-%{version}-py?.?.egg-info

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 4.0.0-1
- Initial package.