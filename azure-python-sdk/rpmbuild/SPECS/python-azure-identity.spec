# Created by pyp2rpm-3.3.2
%global pypi_name azure-identity

Name:           python-%{pypi_name}
Version:        1.4.0b1
Release:        1%{?dist}
Summary:        Microsoft Azure Identity Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/identity/azure-identity
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(azure-core) < 2.0.0
BuildRequires:  python3dist(azure-core) >= 1.0.0
BuildRequires:  python3dist(azure-nspkg)
BuildRequires:  python3dist(cryptography) >= 2.1.4
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(msal) < 2.0.0
BuildRequires:  python3dist(msal) >= 1.0.0
BuildRequires:  python3dist(msal-extensions) >= 0.1.3
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.6
BuildRequires:  python3dist(typing)

%description
 Azure Identity client library for Python Azure Identity authenticating with
Azure Active Directory for Azure SDK libraries. It provides credentials Azure
SDK clients can use to authenticate their requests.This library currently
supports: - [Service principal authentication]( - [Managed identity
authentication]( - User authentication [Source code](

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-core) < 2.0.0
Requires:       python3dist(azure-core) >= 1.0.0
Requires:       python3dist(azure-nspkg)
Requires:       python3dist(cryptography) >= 2.1.4
Requires:       python3dist(mock)
Requires:       python3dist(msal) < 2.0.0
Requires:       python3dist(msal) >= 1.0.0
Requires:       python3dist(msal-extensions) >= 0.1.3
Requires:       python3dist(six) >= 1.6
Requires:       python3dist(typing)
%description -n python3-%{pypi_name}
 Azure Identity client library for Python Azure Identity authenticating with
Azure Active Directory for Azure SDK libraries. It provides credentials Azure
SDK clients can use to authenticate their requests.This library currently
supports: - [Service principal authentication]( - [Managed identity
authentication]( - User authentication [Source code](


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
%{python3_sitelib}/azure_identity-%{version}-py?.?.egg-info

%changelog
* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 1.4.0b1-1
- Upgrade to version 1.4.0b1.

* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 1.3.0-1
- Initial package.