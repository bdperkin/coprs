# Created by pyp2rpm-3.3.2
%global pypi_name azure-mgmt

Name:           python-%{pypi_name}
Version:        4.0.0
Release:        2%{?dist}
Summary:        Microsoft Azure Resource Management Client Libraries for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Microsoft Azure SDK for Python This is the Microsoft Azure Resource Management
bundle.Azure Resource Manager (ARM) is the next generation of management APIs
that replace the old Azure Service Management (ASM).This package does not
contain any code in itself. It installs a set of packages that provide
management APIs for the various Azure services.All packages in this bundle have
been tested...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-mgmt-advisor) >= 1.0
Requires:       python3dist(azure-mgmt-applicationinsights) >= 0.1.1
Requires:       python3dist(azure-mgmt-authorization) >= 0.50.0
Requires:       python3dist(azure-mgmt-batch) >= 5.0
Requires:       python3dist(azure-mgmt-batchai) >= 2.0
Requires:       python3dist(azure-mgmt-billing) >= 0.2.0
Requires:       python3dist(azure-mgmt-cdn) >= 3.0
Requires:       python3dist(azure-mgmt-cognitiveservices) >= 3.0
Requires:       python3dist(azure-mgmt-commerce) >= 1.0
Requires:       python3dist(azure-mgmt-compute) >= 4.0
Requires:       python3dist(azure-mgmt-consumption) >= 2.0
Requires:       python3dist(azure-mgmt-containerinstance) >= 1.0
Requires:       python3dist(azure-mgmt-containerregistry) >= 2.1
Requires:       python3dist(azure-mgmt-containerservice) >= 4.2
Requires:       python3dist(azure-mgmt-cosmosdb) >= 0.4.1
Requires:       python3dist(azure-mgmt-datafactory) >= 0.6.0
Requires:       python3dist(azure-mgmt-datalake-analytics) >= 0.6.0
Requires:       python3dist(azure-mgmt-datalake-store) >= 0.5.0
Requires:       python3dist(azure-mgmt-datamigration) >= 1.0
Requires:       python3dist(azure-mgmt-devspaces) >= 0.1.0
Requires:       python3dist(azure-mgmt-devtestlabs) >= 2.2
Requires:       python3dist(azure-mgmt-dns) >= 2.0
Requires:       python3dist(azure-mgmt-eventgrid) >= 1.0
Requires:       python3dist(azure-mgmt-eventhub) >= 2.1
Requires:       python3dist(azure-mgmt-hanaonazure) >= 0.1.1
Requires:       python3dist(azure-mgmt-iotcentral) >= 0.1.0
Requires:       python3dist(azure-mgmt-iothub) >= 0.5.0
Requires:       python3dist(azure-mgmt-iothubprovisioningservices) >= 0.2.0
Requires:       python3dist(azure-mgmt-keyvault) >= 1.0
Requires:       python3dist(azure-mgmt-loganalytics) >= 0.2.0
Requires:       python3dist(azure-mgmt-logic) >= 3.0
Requires:       python3dist(azure-mgmt-machinelearningcompute) >= 0.4.1
Requires:       python3dist(azure-mgmt-managementgroups) >= 0.1.0
Requires:       python3dist(azure-mgmt-managementpartner) >= 0.1.0
Requires:       python3dist(azure-mgmt-maps) >= 0.1.0
Requires:       python3dist(azure-mgmt-marketplaceordering) >= 0.1.0
Requires:       python3dist(azure-mgmt-media) >= 1.0.0rc2
Requires:       python3dist(azure-mgmt-monitor) >= 0.5.2
Requires:       python3dist(azure-mgmt-msi) >= 0.2.0
Requires:       python3dist(azure-mgmt-network) >= 2.0
Requires:       python3dist(azure-mgmt-notificationhubs) >= 2.0
Requires:       python3dist(azure-mgmt-policyinsights) >= 0.1.0
Requires:       python3dist(azure-mgmt-powerbiembedded) >= 2.0
Requires:       python3dist(azure-mgmt-rdbms) >= 1.2
Requires:       python3dist(azure-mgmt-recoveryservices) >= 0.3.0
Requires:       python3dist(azure-mgmt-recoveryservicesbackup) >= 0.3.0
Requires:       python3dist(azure-mgmt-redis) >= 5.0
Requires:       python3dist(azure-mgmt-relay) >= 0.1.0
Requires:       python3dist(azure-mgmt-reservations) >= 0.2.1
Requires:       python3dist(azure-mgmt-resource) >= 2.0
Requires:       python3dist(azure-mgmt-scheduler) >= 2.0
Requires:       python3dist(azure-mgmt-search) >= 2.0
Requires:       python3dist(azure-mgmt-servicebus) >= 0.5.1
Requires:       python3dist(azure-mgmt-servicefabric) >= 0.2.0
Requires:       python3dist(azure-mgmt-signalr) >= 0.1.0
Requires:       python3dist(azure-mgmt-sql) >= 0.9.1
Requires:       python3dist(azure-mgmt-storage) >= 2.0
Requires:       python3dist(azure-mgmt-subscription) >= 0.2.0
Requires:       python3dist(azure-mgmt-trafficmanager) >= 0.50.0
Requires:       python3dist(azure-mgmt-web) >= 0.35.0
%description -n python3-%{pypi_name}
Microsoft Azure SDK for Python This is the Microsoft Azure Resource Management
bundle.Azure Resource Manager (ARM) is the next generation of management APIs
that replace the old Azure Service Management (ASM).This package does not
contain any code in itself. It installs a set of packages that provide
management APIs for the various Azure services.All packages in this bundle have
been tested...


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

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/azure_mgmt-%{version}-py?.?.egg-info

%changelog
* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 4.0.0-2
- Rebuilt.

* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 4.0.0-1
- Initial package.