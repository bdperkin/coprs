# Created by pyp2rpm-3.3.2
%global pypi_name azure-storage-nspkg

Name:           python-%{pypi_name}
Version:        3.1.0
Release:        1%{?dist}
Summary:        Microsoft Azure Storage Namespace Package [Internal]

License:        MIT License
URL:            https://github.com/Azure/azure-storage-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Microsoft Azure Storage SDK for Python This is the Microsoft Azure Storage
namespace package.This package is not intended to be installed directly by the
end user.It provides the necessary files for other packages to extend the
azure.storage namespace.If you are looking to install the Azure Storage
libraries, see the azure < bundle package.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-nspkg) >= 2.0.0
%description -n python3-%{pypi_name}
Microsoft Azure Storage SDK for Python This is the Microsoft Azure Storage
namespace package.This package is not intended to be installed directly by the
end user.It provides the necessary files for other packages to extend the
azure.storage namespace.If you are looking to install the Azure Storage
libraries, see the azure < bundle package.


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
%{python3_sitelib}/azure_storage_nspkg-%{version}-py?.?.egg-info

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 3.1.0-1
- Initial package.