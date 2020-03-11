# Created by pyp2rpm-3.3.2
%global pypi_name azure-nspkg

Name:           python-%{pypi_name}
Version:        3.0.2
Release:        2%{?dist}
Summary:        Microsoft Azure Namespace Package [Internal]

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Microsoft Azure SDK for Python This is the Microsoft Azure namespace
package.This package is not intended to be installed directly by the end
user.Since version 3.0, this is Python 2 package only, Python 3.x SDKs will use
PEP420 < as namespace package strategy. To avoid issues with package servers
that does not support python_requires, a Python 3 package is installed but is
empty.It provides...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}

%description -n python3-%{pypi_name}
Microsoft Azure SDK for Python This is the Microsoft Azure namespace
package.This package is not intended to be installed directly by the end
user.Since version 3.0, this is Python 2 package only, Python 3.x SDKs will use
PEP420 < as namespace package strategy. To avoid issues with package servers
that does not support python_requires, a Python 3 package is installed but is
empty.It provides...


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
%{python3_sitelib}/azure_nspkg-%{version}-py?.?.egg-info

%changelog
* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.2-2
- Rebuilt.

* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 3.0.2-1
- Initial package.