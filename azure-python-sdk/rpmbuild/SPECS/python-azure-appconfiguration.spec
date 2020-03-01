# Created by pyp2rpm-3.3.2
%global pypi_name azure-appconfiguration

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Microsoft App Configuration Data Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/appconfiguration/azure-appconfiguration
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(aiodns) >= 2.0
BuildRequires:  python3dist(aiohttp) >= 3.0
BuildRequires:  python3dist(azure-core) < 2.0.0
BuildRequires:  python3dist(azure-core) >= 1.0.0
BuildRequires:  python3dist(azure-nspkg)
BuildRequires:  python3dist(msrest) >= 0.6.10
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing)

%description
 Azure App Configuration client library for PythonAzure App Configuration is a
managed service that helps developers centralize their application
configurations simply and securely.Modern programs, especially programs running
in a cloud, generally have many components that are distributed in nature.
Spreading configuration settings across these components can lead to hard-to-
troubleshoot...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(aiodns) >= 2.0
Requires:       python3dist(aiohttp) >= 3.0
Requires:       python3dist(azure-core) < 2.0.0
Requires:       python3dist(azure-core) >= 1.0.0
Requires:       python3dist(azure-nspkg)
Requires:       python3dist(msrest) >= 0.6.10
Requires:       python3dist(typing)
%description -n python3-%{pypi_name}
 Azure App Configuration client library for PythonAzure App Configuration is a
managed service that helps developers centralize their application
configurations simply and securely.Modern programs, especially programs running
in a cloud, generally have many components that are distributed in nature.
Spreading configuration settings across these components can lead to hard-to-
troubleshoot...


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
%{python3_sitelib}/azure_appconfiguration-%{version}-py?.?.egg-info

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 1.0.0-1
- Initial package.