# Created by pyp2rpm-3.3.2
%global pypi_name msal-extensions

Name:           python-%{pypi_name}
Version:        0.1.3
Release:        1%{?dist}
Summary:        %{pypi_name}

License:        None
URL:            None
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(msal) < 2.0.0
BuildRequires:  python3dist(msal) >= 0.4.1
BuildRequires:  python3dist(portalocker) >= 1.0
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(msal) < 2.0.0
Requires:       python3dist(msal) >= 0.4.1
Requires:       python3dist(portalocker) >= 1.0
%description -n python3-%{pypi_name}



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
%{python3_sitelib}/msal_extensions
%{python3_sitelib}/msal_extensions-%{version}-py?.?.egg-info

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 0.1.3-1
- Initial package.