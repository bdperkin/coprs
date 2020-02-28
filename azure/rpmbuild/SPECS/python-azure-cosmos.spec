# Created by pyp2rpm-3.3.2
%global pypi_name azure-cosmos

Name:           python-%{pypi_name}
Version:        3.1.2
Release:        1%{?dist}
Summary:        Azure Cosmos Python SDK

License:        MIT
URL:            https://github.com/Azure/azure-documentdb-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(requests) >= 2.10.0
BuildRequires:  python2dist(setuptools)
BuildRequires:  python2dist(six) >= 1.6
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(requests) >= 2.10.0
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.6
BuildRequires:  python3dist(sphinx)

%description
 Azure Cosmos DB SQL API client library for PythonAzure Cosmos DB is a globally
distributed, multi-model database service that supports document, key-value,
wide-column, and graph databases.Use the Azure Cosmos DB SQL API SDK for Python
to manage databases and the JSON documents they contain in this NoSQL database
service.* Create Cosmos DB **databases** and modify their settings * Create
and...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(requests) >= 2.10.0
Requires:       python2dist(six) >= 1.6
%description -n python2-%{pypi_name}
 Azure Cosmos DB SQL API client library for PythonAzure Cosmos DB is a globally
distributed, multi-model database service that supports document, key-value,
wide-column, and graph databases.Use the Azure Cosmos DB SQL API SDK for Python
to manage databases and the JSON documents they contain in this NoSQL database
service.* Create Cosmos DB **databases** and modify their settings * Create
and...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(requests) >= 2.10.0
Requires:       python3dist(six) >= 1.6
%description -n python3-%{pypi_name}
 Azure Cosmos DB SQL API client library for PythonAzure Cosmos DB is a globally
distributed, multi-model database service that supports document, key-value,
wide-column, and graph databases.Use the Azure Cosmos DB SQL API SDK for Python
to manage databases and the JSON documents they contain in this NoSQL database
service.* Create Cosmos DB **databases** and modify their settings * Create
and...

%package -n python-%{pypi_name}-doc
Summary:        azure-cosmos documentation
%description -n python-%{pypi_name}-doc
Documentation for azure-cosmos

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 doc html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python2_sitelib}/azure
%{python2_sitelib}/doc
%{python2_sitelib}/samples
%{python2_sitelib}/azure_cosmos-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/azure
%{python3_sitelib}/doc
%{python3_sitelib}/samples
%{python3_sitelib}/azure_cosmos-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
* Tue Feb 25 2020 mockbuilder - 3.1.2-1
- Initial package.