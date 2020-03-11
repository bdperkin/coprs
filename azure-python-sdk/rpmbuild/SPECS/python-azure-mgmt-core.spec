# Created by pyp2rpm-3.3.2
%global pypi_name azure-mgmt-core

Name:           python-%{pypi_name}
Version:        1.0.0b1
Release:        2%{?dist}
Summary:        Microsoft Azure Management Core Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/core/azure-mgmt-core
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(azure-core) < 2.0.0
BuildRequires:  python3dist(azure-core) >= 1.3.0
BuildRequires:  python3dist(azure-mgmt-nspkg)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing)

%description
 Azure Management Core LibraryAzure management core library defines extensions
to Azure Core that are specific to ARM (Azure Resource Management) needed when
you use client libraries.As an end user, you don't need to manually install
azure-mgmt-core because it will be installed automatically when you install
other SDKs.[Source code]() | [Package (Pypi)][package] | [API reference...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-core) < 2.0.0
Requires:       python3dist(azure-core) >= 1.3.0
Requires:       python3dist(azure-mgmt-nspkg)
Requires:       python3dist(typing)
%description -n python3-%{pypi_name}
 Azure Management Core LibraryAzure management core library defines extensions
to Azure Core that are specific to ARM (Azure Resource Management) needed when
you use client libraries.As an end user, you don't need to manually install
azure-mgmt-core because it will be installed automatically when you install
other SDKs.[Source code]() | [Package (Pypi)][package] | [API reference...


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
%license LICENSE.md
%doc README.md
%{python3_sitelib}/azure
%{python3_sitelib}/azure_mgmt_core-%{version}-py?.?.egg-info

%changelog
* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 1.0.0b1-2
- Rebuilt.

* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 1.0.0b1-1
- Initial package.