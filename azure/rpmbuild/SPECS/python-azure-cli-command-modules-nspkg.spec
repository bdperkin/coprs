# Created by pyp2rpm-3.3.2
%global pypi_name azure-cli-command-modules-nspkg

Name:           python-%{pypi_name}
Version:        2.0.3
Release:        1%{?dist}
Summary:        Microsoft Azure CLI Command Modules Namespace Package

License:        MIT
URL:            https://github.com/Azure/azure-cli
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Microsoft Azure CLI Command modules Namespace Package This is the Microsoft
Azure CLI command module namespace package.This package is not intended to be
installed directly by the end user.It provides the necessary files for other
packages to extend the azure cli command module namespaces. ..
:changelog:Release History +++++ * Indicate Python 3.7 support.2.0.2* Minor
fixes.2.0.1* minor...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(azure-cli-nspkg) >= 3.0.0
%description -n python2-%{pypi_name}
Microsoft Azure CLI Command modules Namespace Package This is the Microsoft
Azure CLI command module namespace package.This package is not intended to be
installed directly by the end user.It provides the necessary files for other
packages to extend the azure cli command module namespaces. ..
:changelog:Release History +++++ * Indicate Python 3.7 support.2.0.2* Minor
fixes.2.0.1* minor...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(azure-cli-nspkg) >= 3.0.0
%description -n python3-%{pypi_name}
Microsoft Azure CLI Command modules Namespace Package This is the Microsoft
Azure CLI command module namespace package.This package is not intended to be
installed directly by the end user.It provides the necessary files for other
packages to extend the azure cli command module namespaces. ..
:changelog:Release History +++++ * Indicate Python 3.7 support.2.0.2* Minor
fixes.2.0.1* minor...


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
%doc README.rst
%{python2_sitelib}/azure
%{python2_sitelib}/azure_cli_command_modules_nspkg-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/azure
%{python3_sitelib}/azure_cli_command_modules_nspkg-%{version}-py?.?.egg-info

%changelog
* Tue Feb 25 2020 mockbuilder - 2.0.3-1
- Initial package.