# Created by pyp2rpm-3.3.2
%global pypi_name vsts-cd-manager

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        1%{?dist}
Summary:        Python wrapper around some of the VSTS APIs

License:        None
URL:            https://github.com/microsoft/vsts-cd-manager
Source0:        https://files.pythonhosted.org/packages/source/v/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(mock)
Requires:       python3dist(msrest) >= 0.2.0
%description -n python3-%{pypi_name}



%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/aex_accounts
%{python3_sitelib}/continuous_delivery
%{python3_sitelib}/vsts_cd_manager
%{python3_sitelib}/vsts_info_provider
%{python3_sitelib}/vsts_cd_manager-%{version}-py?.?.egg-info

%changelog
* Tue Feb 25 2020 mockbuilder - 1.0.2-1
- Initial package.