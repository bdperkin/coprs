# Created by pyp2rpm-3.3.2
%global pypi_name azure-cosmos

Name:           python-%{pypi_name}
Version:        4.0.0b6
Release:        1%{?dist}
Summary:        Microsoft Azure Cosmos Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(azure-core) < 2.0.0
BuildRequires:  python3dist(azure-core) >= 1.0.0
BuildRequires:  python3dist(azure-nspkg)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.6
BuildRequires:  python3dist(typing)

%description
 Azure Cosmos DB SQL API client library for PythonAzure Cosmos DB is a globally
distributed, multi-model database service that supports document, key-value,
wide-column, and graph databases.Use the Azure Cosmos DB SQL API SDK for Python
to manage databases and the JSON documents they contain in this NoSQL database
service.* Create Cosmos DB **databases** and modify their settings * Create
and...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-core) < 2.0.0
Requires:       python3dist(azure-core) >= 1.0.0
Requires:       python3dist(azure-nspkg)
Requires:       python3dist(six) >= 1.6
Requires:       python3dist(typing)
%description -n python3-%{pypi_name}
 Azure Cosmos DB SQL API client library for PythonAzure Cosmos DB is a globally
distributed, multi-model database service that supports document, key-value,
wide-column, and graph databases.Use the Azure Cosmos DB SQL API SDK for Python
to manage databases and the JSON documents they contain in this NoSQL database
service.* Create Cosmos DB **databases** and modify their settings * Create
and...


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
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/azure
%{python3_sitelib}/doc
%{python3_sitelib}/samples
%{python3_sitelib}/azure_cosmos-%{version}-py?.?.egg-info

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 4.0.0b6-1
- Initial package.