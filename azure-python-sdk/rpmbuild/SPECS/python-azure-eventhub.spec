# Created by pyp2rpm-3.3.2
%global pypi_name azure-eventhub

Name:           python-%{pypi_name}
Version:        5.0.1
Release:        2%{?dist}
Summary:        Microsoft Azure Event Hubs Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/eventhub/azure-eventhub
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(azure-core) < 2.0.0
BuildRequires:  python3dist(azure-core) >= 1.0.0
BuildRequires:  python3dist(azure-nspkg)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing)
BuildRequires:  python3dist(uamqp) < 2.0
BuildRequires:  python3dist(uamqp) >= 1.2.5

%description
 Azure Event Hubs client library for PythonAzure Event Hubs is a highly
scalable publish-subscribe service that can ingest millions of events per
second and stream them to multiple consumers. This lets you process and analyze
the massive amounts of data produced by your connected devices and
applications. Once Event Hubs has collected the data, you can retrieve,
transform, and store it by...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-core) < 2.0.0
Requires:       python3dist(azure-core) >= 1.0.0
Requires:       python3dist(azure-nspkg)
Requires:       python3dist(typing)
Requires:       python3dist(uamqp) < 2.0
Requires:       python3dist(uamqp) >= 1.2.5
%description -n python3-%{pypi_name}
 Azure Event Hubs client library for PythonAzure Event Hubs is a highly
scalable publish-subscribe service that can ingest millions of events per
second and stream them to multiple consumers. This lets you process and analyze
the massive amounts of data produced by your connected devices and
applications. Once Event Hubs has collected the data, you can retrieve,
transform, and store it by...


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
%{python3_sitelib}/azure_eventhub-%{version}-py?.?.egg-info

%changelog
* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 5.0.1-2
- Rebuilt.

* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 5.0.1-1
- Initial package.