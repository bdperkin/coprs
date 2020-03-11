# Created by pyp2rpm-3.3.2
%global pypi_name azure-search

Name:           python-%{pypi_name}
Version:        1.0.0b1
Release:        2%{?dist}
Summary:        Microsoft Azure Cognitive Search Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/search/azure-search
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(azure-core) < 2.0.0
BuildRequires:  python3dist(azure-core) >= 1.2.2
BuildRequires:  python3dist(azure-nspkg)
BuildRequires:  python3dist(msrest) >= 0.6.10
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing)

%description
 Azure Cognitive Search client library for PythonAzure Cognitive Search is a
fully managed cloud search service that provides a rich search experience to
custom applications.[Source code]( | [Package (PyPI)]( | [API reference
documentation]( | [Product documentation]( | [Samples]( Getting started
Prerequisites

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-core) < 2.0.0
Requires:       python3dist(azure-core) >= 1.2.2
Requires:       python3dist(azure-nspkg)
Requires:       python3dist(msrest) >= 0.6.10
Requires:       python3dist(typing)
%description -n python3-%{pypi_name}
 Azure Cognitive Search client library for PythonAzure Cognitive Search is a
fully managed cloud search service that provides a rich search experience to
custom applications.[Source code]( | [Package (PyPI)]( | [API reference
documentation]( | [Product documentation]( | [Samples]( Getting started
Prerequisites


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
%doc README.md samples/README.md
%{python3_sitelib}/azure
%{python3_sitelib}/azure_search-%{version}-py?.?.egg-info

%changelog
* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 1.0.0b1-2
- Rebuilt.

* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 1.0.0b1-1
- Initial package.