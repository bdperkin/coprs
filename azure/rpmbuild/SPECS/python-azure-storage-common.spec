# Created by pyp2rpm-3.3.2
%global pypi_name azure-storage-common

Name:           python-%{pypi_name}
Version:        1.4.2
Release:        1%{?dist}
Summary:        Microsoft Azure Storage Common Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-storage-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Microsoft Azure Storage SDK for Python This project provides a client library
in Python that makes it easy to consume Microsoft Azure Storage services. For
documentation please see the Microsoft Azure Python Developer Center_ and our
API Reference_ (also available on readthedocs_). If you are looking for the
Service Bus or Azure Management

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(azure-common) >= 1.1.5
Requires:       python2dist(azure-storage-nspkg)
Requires:       python2dist(cryptography)
Requires:       python2dist(python-dateutil)
Requires:       python2dist(requests)
%description -n python2-%{pypi_name}
Microsoft Azure Storage SDK for Python This project provides a client library
in Python that makes it easy to consume Microsoft Azure Storage services. For
documentation please see the Microsoft Azure Python Developer Center_ and our
API Reference_ (also available on readthedocs_). If you are looking for the
Service Bus or Azure Management

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(azure-common) >= 1.1.5
Requires:       python3dist(azure-storage-nspkg)
Requires:       python3dist(cryptography)
Requires:       python3dist(python-dateutil)
Requires:       python3dist(requests)
%description -n python3-%{pypi_name}
Microsoft Azure Storage SDK for Python This project provides a client library
in Python that makes it easy to consume Microsoft Azure Storage services. For
documentation please see the Microsoft Azure Python Developer Center_ and our
API Reference_ (also available on readthedocs_). If you are looking for the
Service Bus or Azure Management


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
%py3_install

%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/azure
%{python2_sitelib}/azure_storage_common-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/azure
%{python3_sitelib}/azure_storage_common-%{version}-py?.?.egg-info

%changelog
* Tue Feb 25 2020 mockbuilder - 1.4.2-1
- Initial package.