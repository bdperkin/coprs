# Created by pyp2rpm-3.3.2
%global pypi_name azure-storage-blob

Name:           python-%{pypi_name}
Version:        12.2.0
Release:        1%{?dist}
Summary:        Microsoft Azure Blob Storage Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-blob
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(azure-core) < 2.0.0
BuildRequires:  python3dist(azure-core) >= 1.2.2
BuildRequires:  python3dist(azure-storage-nspkg) < 4.0.0
BuildRequires:  python3dist(azure-storage-nspkg) >= 3.0.0
BuildRequires:  python3dist(cryptography) >= 2.1.4
BuildRequires:  python3dist(msrest) >= 0.6.10
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing)

%description
 Azure Storage Blobs client library for Python Azure Blob storage is
Microsoft's object storage solution for the cloud. Blob storage is optimized
for storing massive amounts of unstructured data, such as text or binary
data.Blob storage is ideal for:* Serving images or documents directly to a
browser * Storing files for distributed access * Streaming video and audio *
Storing data for backup...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-core) < 2.0.0
Requires:       python3dist(azure-core) >= 1.2.2
Requires:       python3dist(azure-storage-nspkg) < 4.0.0
Requires:       python3dist(azure-storage-nspkg) >= 3.0.0
Requires:       python3dist(cryptography) >= 2.1.4
Requires:       python3dist(msrest) >= 0.6.10
Requires:       python3dist(typing)
%description -n python3-%{pypi_name}
 Azure Storage Blobs client library for Python Azure Blob storage is
Microsoft's object storage solution for the cloud. Blob storage is optimized
for storing massive amounts of unstructured data, such as text or binary
data.Blob storage is ideal for:* Serving images or documents directly to a
browser * Storing files for distributed access * Streaming video and audio *
Storing data for backup...


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
%{python3_sitelib}/azure_storage_blob-%{version}-py?.?.egg-info

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 12.2.0-1
- Initial package.