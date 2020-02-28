# Created by pyp2rpm-3.3.2
%global pypi_name bashbeautify

Name:           python-%{pypi_name}
Version:        0.1.8
Release:        1%{?dist}
Summary:        A beautifier for Bash shell scripts written in Python

License:        GPLv2
URL:            https://github.com/hermanbergwerf/bashbeautify
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description


%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(argparse)
Requires:       python2dist(setuptools)
%description -n python2-%{pypi_name}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(argparse)
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}



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
rm -rf %{buildroot}%{_bindir}/*
%py3_install

%files -n python2-%{pypi_name}
%doc README.md
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.md
%{_bindir}/bashbeautify
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Feb 20 2020 mockbuilder - 0.1.8-1
- Initial package.