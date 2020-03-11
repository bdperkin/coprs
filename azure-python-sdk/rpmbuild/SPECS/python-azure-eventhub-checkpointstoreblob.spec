# Created by pyp2rpm-3.3.2
%global pypi_name azure-eventhub-checkpointstoreblob

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        2%{?dist}
Summary:        Microsoft Azure Event Hubs checkpointer implementation with Blob Storage Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/eventhub/azure-eventhub-checkpointstoreblob
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(azure-core) < 2.0.0
BuildRequires:  python3dist(azure-core) >= 1.2.2
BuildRequires:  python3dist(azure-eventhub) < 6.0.0
BuildRequires:  python3dist(azure-eventhub) >= 5.0.0
BuildRequires:  python3dist(cryptography) >= 2.1.4
BuildRequires:  python3dist(msrest) >= 0.6.10
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing)

%description
 Azure EventHubs Checkpoint Store client library for Python using Storage
BlobsAzure EventHubs Checkpoint Store is used for storing checkpoints while
processing events from Azure Event Hubs. This Checkpoint Store package works as
a plug-in package to EventHubConsumerClient. It uses Azure Storage Blob as the
persistent store for maintaining checkpoints and partition ownership
information.Please...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-core) < 2.0.0
Requires:       python3dist(azure-core) >= 1.2.2
Requires:       python3dist(azure-eventhub) < 6.0.0
Requires:       python3dist(azure-eventhub) >= 5.0.0
Requires:       python3dist(cryptography) >= 2.1.4
Requires:       python3dist(msrest) >= 0.6.10
Requires:       python3dist(typing)
%description -n python3-%{pypi_name}
 Azure EventHubs Checkpoint Store client library for Python using Storage
BlobsAzure EventHubs Checkpoint Store is used for storing checkpoints while
processing events from Azure Event Hubs. This Checkpoint Store package works as
a plug-in package to EventHubConsumerClient. It uses Azure Storage Blob as the
persistent store for maintaining checkpoints and partition ownership
information.Please...


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
%{python3_sitelib}/azure
%{python3_sitelib}/azure_eventhub_checkpointstoreblob-%{version}-py?.?.egg-info

%changelog
* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.0-2
- Rebuilt.

* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.0-1
- Initial package.