# Created by pyp2rpm-3.3.2
%global pypi_name argparse

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        1%{?dist}
Summary:        Python command-line parsing library

License:        Python Software Foundation License
URL:            https://github.com/ThomasWaldmann/argparse/
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
The argparse module makes it easy to write user friendly command line
interfaces.The program defines what arguments it requires, and argparse will
figure out how to parse those out of sys.argv. The argparse module also
automatically generates help and usage messages and issues errors when users
give the program invalid arguments.As of Python > 2.7 and > 3.2, the argparse
module is maintained...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
The argparse module makes it easy to write user friendly command line
interfaces.The program defines what arguments it requires, and argparse will
figure out how to parse those out of sys.argv. The argparse module also
automatically generates help and usage messages and issues errors when users
give the program invalid arguments.As of Python > 2.7 and > 3.2, the argparse
module is maintained...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The argparse module makes it easy to write user friendly command line
interfaces.The program defines what arguments it requires, and argparse will
figure out how to parse those out of sys.argv. The argparse module also
automatically generates help and usage messages and issues errors when users
give the program invalid arguments.As of Python > 2.7 and > 3.2, the argparse
module is maintained...

%package -n python-%{pypi_name}-doc
Summary:        argparse documentation
%description -n python-%{pypi_name}-doc
Documentation for argparse

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE.txt doc/source/Python-License.txt doc/source/license.rst
%doc README.txt
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.txt doc/source/Python-License.txt doc/source/license.rst
%doc README.txt
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt doc/source/Python-License.txt doc/source/license.rst

%changelog
* Thu Feb 20 2020 mockbuilder - 1.4.0-1
- Initial package.