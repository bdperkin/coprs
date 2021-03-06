# Created by pyp2rpm-3.3.2
%global pypi_name azure-servicebus

Name:           python-%{pypi_name}
Version:        0.50.2
Release:        2%{?dist}
Summary:        Microsoft Azure Service Bus Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Microsoft Azure Service Bus SDK for Python This is the Microsoft Azure Service
Bus Client Library. This package has been tested with Python 2.7, 3.4, 3.5, 3.6
and 3.7.Microsoft Azure Service Bus supports a set of cloud-based, message-
oriented middleware technologies including reliable message queuing and durable
publish/subscribe messaging.* SDK source code < * SDK reference documentation <
*...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-common) >= 1.1
Requires:       python3dist(azure-nspkg)
Requires:       python3dist(msrestazure) < 2.0.0
Requires:       python3dist(msrestazure) >= 0.4.32
Requires:       python3dist(uamqp) < 2.0.0
Requires:       python3dist(uamqp) >= 1.2.5
%description -n python3-%{pypi_name}
Microsoft Azure Service Bus SDK for Python This is the Microsoft Azure Service
Bus Client Library. This package has been tested with Python 2.7, 3.4, 3.5, 3.6
and 3.7.Microsoft Azure Service Bus supports a set of cloud-based, message-
oriented middleware technologies including reliable message queuing and durable
publish/subscribe messaging.* SDK source code < * SDK reference documentation <
*...


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
%{python3_sitelib}/azure
%{python3_sitelib}/azure_servicebus-%{version}-py?.?.egg-info

%changelog
* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 0.50.2-2
- Rebuilt.

* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 0.50.2-1
- Initial package.