# Created by pyp2rpm-3.3.2
%global pypi_name azure-storage-file-datalake

Name:           python-%{pypi_name}
Version:        12.0.0b7
Release:        2%{?dist}
Summary:        Microsoft Azure File DataLake Storage Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(azure-core) < 2.0.0
BuildRequires:  python3dist(azure-core) >= 1.2.2
BuildRequires:  python3dist(azure-storage-blob) >= 12.0
BuildRequires:  python3dist(azure-storage-nspkg) < 4.0.0
BuildRequires:  python3dist(azure-storage-nspkg) >= 3.0.0
BuildRequires:  python3dist(msrest) >= 0.6.10
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing)

%description
 Azure DataLake service client library for Python This preview package for
Python includes ADLS Gen2 specific API support made available in Storage SDK.
This includes: 1. New directory level operations (Create, Rename, Delete) for
hierarchical namespace enabled (HNS) storage account. For HNS enabled accounts,
the rename/move operations are atomic. 2. Permission related operations
(Get/Set...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-core) < 2.0.0
Requires:       python3dist(azure-core) >= 1.2.2
Requires:       python3dist(azure-storage-blob) >= 12.0
Requires:       python3dist(azure-storage-nspkg) < 4.0.0
Requires:       python3dist(azure-storage-nspkg) >= 3.0.0
Requires:       python3dist(msrest) >= 0.6.10
Requires:       python3dist(typing)
%description -n python3-%{pypi_name}
 Azure DataLake service client library for Python This preview package for
Python includes ADLS Gen2 specific API support made available in Storage SDK.
This includes: 1. New directory level operations (Create, Rename, Delete) for
hierarchical namespace enabled (HNS) storage account. For HNS enabled accounts,
the rename/move operations are atomic. 2. Permission related operations
(Get/Set...


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
%{python3_sitelib}/azure_storage_file_datalake-%{version}-py?.?.egg-info

%changelog
* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 12.0.0b7-2
- Rebuilt.

* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 12.0.0b7-1
- Initial package.