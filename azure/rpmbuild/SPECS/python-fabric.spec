# Created by pyp2rpm-3.3.2
%global pypi_name fabric

Name:           python-%{pypi_name}
Version:        2.5.0
Release:        1%{?dist}
Summary:        High level SSH command execution

License:        BSD
URL:            http://fabfile.org
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
To find out what's new in this version of Fabric, please see the changelog < to
Fabric! Fabric is a high level Python (2.7, 3.4+) library designed to execute
shell commands remotely over SSH, yielding useful Python objects in return. It
builds on top of Invoke <>_ (subprocess command execution and command-line
features) and Paramiko <>_ (SSH protocol implementation), extending their APIs
to...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(invoke) < 2.0
Requires:       python2dist(invoke) >= 1.3
Requires:       python2dist(mock) < 3.0
Requires:       python2dist(mock) < 3.0
Requires:       python2dist(mock) >= 2.0.0
Requires:       python2dist(mock) >= 2.0.0
Requires:       python2dist(paramiko) >= 2.4
Requires:       python2dist(pytest) < 4.0
Requires:       python2dist(pytest) >= 3.2.5
Requires:       python2dist(setuptools)
%description -n python2-%{pypi_name}
To find out what's new in this version of Fabric, please see the changelog < to
Fabric! Fabric is a high level Python (2.7, 3.4+) library designed to execute
shell commands remotely over SSH, yielding useful Python objects in return. It
builds on top of Invoke <>_ (subprocess command execution and command-line
features) and Paramiko <>_ (SSH protocol implementation), extending their APIs
to...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(invoke) < 2.0
Requires:       python3dist(invoke) >= 1.3
Requires:       python3dist(mock) < 3.0
Requires:       python3dist(mock) < 3.0
Requires:       python3dist(mock) >= 2.0.0
Requires:       python3dist(mock) >= 2.0.0
Requires:       python3dist(paramiko) >= 2.4
Requires:       python3dist(pytest) < 4.0
Requires:       python3dist(pytest) >= 3.2.5
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
To find out what's new in this version of Fabric, please see the changelog < to
Fabric! Fabric is a high level Python (2.7, 3.4+) library designed to execute
shell commands remotely over SSH, yielding useful Python objects in return. It
builds on top of Invoke <>_ (subprocess command execution and command-line
features) and Paramiko <>_ (SSH protocol implementation), extending their APIs
to...

%package -n python-%{pypi_name}-doc
Summary:        fabric documentation
%description -n python-%{pypi_name}-doc
Documentation for fabric

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
%{_bindir}/fab
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Feb 25 2020 mockbuilder - 2.5.0-1
- Initial package.