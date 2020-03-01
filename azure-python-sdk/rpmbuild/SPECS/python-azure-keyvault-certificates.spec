# Created by pyp2rpm-3.3.2
%global pypi_name azure-keyvault-certificates

Name:           python-%{pypi_name}
Version:        4.0.1
Release:        1%{?dist}
Summary:        Microsoft Azure Key Vault Certificates Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-certificates
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(azure-common) >= 1.1
BuildRequires:  python3dist(azure-core) < 2.0.0
BuildRequires:  python3dist(azure-core) >= 1.2.1
BuildRequires:  python3dist(azure-keyvault-nspkg)
BuildRequires:  python3dist(msrest) >= 0.6.0
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing)

%description
 Azure Key Vault Certificates client library for Python Azure Key Vault helps
solve the following problems: - Certificate management (this library) - create,
manage, and deploy public and private SSL/TLS certificates - Cryptographic key
management ([azure-keyvault-keys]( - create, store, and control access to the
keys used to encrypt your data - Secrets management ([azure-keyvault-secrets](
-...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-common) >= 1.1
Requires:       python3dist(azure-core) < 2.0.0
Requires:       python3dist(azure-core) >= 1.2.1
Requires:       python3dist(azure-keyvault-nspkg)
Requires:       python3dist(msrest) >= 0.6.0
Requires:       python3dist(typing)
%description -n python3-%{pypi_name}
 Azure Key Vault Certificates client library for Python Azure Key Vault helps
solve the following problems: - Certificate management (this library) - create,
manage, and deploy public and private SSL/TLS certificates - Cryptographic key
management ([azure-keyvault-keys]( - create, store, and control access to the
keys used to encrypt your data - Secrets management ([azure-keyvault-secrets](
-...


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

%check
%{__python3} setup.py test || true

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/azure
%{python3_sitelib}/azure_keyvault_certificates-%{version}-py?.?.egg-info

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 4.0.1-1
- Initial package.