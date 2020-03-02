# Created by pyp2rpm-3.3.2
%global pypi_name azure-storage-queue

Name:           python-%{pypi_name}
Version:        12.1.0
Release:        1%{?dist}
Summary:        Microsoft Azure Azure Queue Storage Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/storage/azure-storage-queue
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(azure-core) < 2.0.0
BuildRequires:  python3dist(azure-core) >= 1.1.0
BuildRequires:  python3dist(azure-storage-nspkg) < 4.0.0
BuildRequires:  python3dist(azure-storage-nspkg) >= 3.0.0
BuildRequires:  python3dist(cryptography) >= 2.1.4
BuildRequires:  python3dist(msrest) >= 0.6.10
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing)

%description
 Azure Storage Queues client library for PythonAzure Queue storage is a service
for storing large numbers of messages that can be accessed from anywhere in the
world via authenticated calls using HTTP or HTTPS. A single queue message can
be up to 64 KiB in size, and a queue can contain millions of messages, up to
the total capacity limit of a storage account.Common uses of Queue storage...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-core) < 2.0.0
Requires:       python3dist(azure-core) >= 1.1.0
Requires:       python3dist(azure-storage-nspkg) < 4.0.0
Requires:       python3dist(azure-storage-nspkg) >= 3.0.0
Requires:       python3dist(cryptography) >= 2.1.4
Requires:       python3dist(msrest) >= 0.6.10
Requires:       python3dist(typing)
%description -n python3-%{pypi_name}
 Azure Storage Queues client library for PythonAzure Queue storage is a service
for storing large numbers of messages that can be accessed from anywhere in the
world via authenticated calls using HTTP or HTTPS. A single queue message can
be up to 64 KiB in size, and a queue can contain millions of messages, up to
the total capacity limit of a storage account.Common uses of Queue storage...


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
%{python3_sitelib}/azure_storage_queue-%{version}-py?.?.egg-info

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 12.1.0-1
- Initial package.