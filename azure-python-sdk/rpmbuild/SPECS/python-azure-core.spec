# Created by pyp2rpm-3.3.2
%global pypi_name azure-core

Name:           python-%{pypi_name}
Version:        1.2.2
Release:        1%{?dist}
Summary:        Microsoft Azure Core Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/core/azure-core
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(azure-nspkg)
BuildRequires:  python3dist(requests) >= 2.18.4
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.6
BuildRequires:  python3dist(typing)

%description
 Azure Core LibraryAzure core library defines basic exceptions and shared
modules those are needed when you use client libraries. As an end user, you
don't need to manually install azure-core because it will be installed
automatically when you install other SDKs. If you are a client library
developer, please reference [client library developer reference]( for more
information.[Source code]( |...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-nspkg)
Requires:       python3dist(requests) >= 2.18.4
Requires:       python3dist(six) >= 1.6
Requires:       python3dist(typing)
%description -n python3-%{pypi_name}
 Azure Core LibraryAzure core library defines basic exceptions and shared
modules those are needed when you use client libraries. As an end user, you
don't need to manually install azure-core because it will be installed
automatically when you install other SDKs. If you are a client library
developer, please reference [client library developer reference]( for more
information.[Source code]( |...


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
%doc README.md samples/README.md
%{python3_sitelib}/azure
%{python3_sitelib}/azure_core-%{version}-py?.?.egg-info

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.2-1
- Initial package.