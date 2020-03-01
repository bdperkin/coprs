# Created by pyp2rpm-3.3.2
%global pypi_name msal

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        1%{?dist}
Summary:        The Microsoft Authentication Library (MSAL) for Python library enables your app to access the Microsoft Cloud by supporting authentication of users with Microsoft Azure Active Directory accounts (AAD) and Microsoft Accounts (MSA) using industry standard OAuth2 and OpenID Connect

License:        MIT
URL:            https://github.com/AzureAD/microsoft-authentication-library-for-python
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Microsoft Authentication Library (MSAL) for Python | dev branch | Reference
Docs || [![Build status]( | [![Documentation Status]( Microsoft Authentication
Library for Python enables applications to integrate with the [Microsoft
identity platform]( It allows you to sign in users or apps with Microsoft
identities ([Azure AD]( [Microsoft Accounts]() and [Azure AD B2C]( accounts)
and obtain...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(pyjwt) < 2
Requires:       python3dist(pyjwt) >= 1.0.0
Requires:       python3dist(requests) < 3
Requires:       python3dist(requests) >= 2.0.0
%description -n python3-%{pypi_name}
 Microsoft Authentication Library (MSAL) for Python | dev branch | Reference
Docs || [![Build status]( | [![Documentation Status]( Microsoft Authentication
Library for Python enables applications to integrate with the [Microsoft
identity platform]( It allows you to sign in users or apps with Microsoft
identities ([Azure AD]( [Microsoft Accounts]() and [Azure AD B2C]( accounts)
and obtain...


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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.0-1
- Initial package.