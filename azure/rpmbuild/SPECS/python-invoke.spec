# Created by pyp2rpm-3.3.2
%global pypi_name invoke

Name:           python-%{pypi_name}
Version:        1.4.1
Release:        1%{?dist}
Summary:        Pythonic task execution

License:        BSD
URL:            http://docs.pyinvoke.org
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
To find out what's new in this version of Invoke, please see the changelog < to
Invoke! Invoke is a Python (2.7 and 3.4+) library for managing shell-oriented
subprocesses and organizing executable Python code into CLI-invokable tasks. It
draws inspiration from various sources (make/rake, Fabric 1.x, etc) to arrive
at a powerful & clean feature set.For a high level introduction, including...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(setuptools)
%description -n python2-%{pypi_name}
To find out what's new in this version of Invoke, please see the changelog < to
Invoke! Invoke is a Python (2.7 and 3.4+) library for managing shell-oriented
subprocesses and organizing executable Python code into CLI-invokable tasks. It
draws inspiration from various sources (make/rake, Fabric 1.x, etc) to arrive
at a powerful & clean feature set.For a high level introduction, including...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
To find out what's new in this version of Invoke, please see the changelog < to
Invoke! Invoke is a Python (2.7 and 3.4+) library for managing shell-oriented
subprocesses and organizing executable Python code into CLI-invokable tasks. It
draws inspiration from various sources (make/rake, Fabric 1.x, etc) to arrive
at a powerful & clean feature set.For a high level introduction, including...

%package -n python-%{pypi_name}-doc
Summary:        invoke documentation
%description -n python-%{pypi_name}-doc
Documentation for invoke

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 sites/docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
rm -rf %{buildroot}%{_bindir}/*
%py3_install

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/inv
%{_bindir}/invoke
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Feb 25 2020 mockbuilder - 1.4.1-1
- Initial package.