# Created by pyp2rpm-3.3.2
%global pypi_name jsondiff

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Diff JSON and JSON-like structures in Python

License:        None
URL:            https://github.com/ZoomerAnalytics/jsondiff
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(setuptools)
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
%license LICENSE
%doc README.rst tests/generate_readme.py
%{_bindir}/jdiff
%{_bindir}/jsondiff
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Feb 25 2020 mockbuilder - 1.2.0-1
- Initial package.