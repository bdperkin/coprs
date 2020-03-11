# Created by pyp2rpm-3.3.2
%global pypi_name azure-common

Name:           python-%{pypi_name}
Version:        1.1.25
Release:        1%{?dist}
Summary:        Microsoft Azure Client Library for Python (Common)

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Microsoft Azure SDK for PythonThis is the Microsoft Azure common code.This
package provides shared code by the Azure packages.If you are looking to
install the Azure client libraries, refer to the main Github repository:
![Impressions]( Release History 1.1.25 (2020-03-09)-
get_client_from_cli_profile no longer requires "azure-core" if not necessary
1.1.24 (2019-12-18)-...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-nspkg)
%description -n python3-%{pypi_name}
 Microsoft Azure SDK for PythonThis is the Microsoft Azure common code.This
package provides shared code by the Azure packages.If you are looking to
install the Azure client libraries, refer to the main Github repository:
![Impressions]( Release History 1.1.25 (2020-03-09)-
get_client_from_cli_profile no longer requires "azure-core" if not necessary
1.1.24 (2019-12-18)-...


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
%doc README.md
%{python3_sitelib}/azure
%{python3_sitelib}/azure_common-%{version}-py?.?.egg-info

%changelog
* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.25-1
- Upgrade to version 1.1.25.

* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 1.1.24-1
- Initial package.