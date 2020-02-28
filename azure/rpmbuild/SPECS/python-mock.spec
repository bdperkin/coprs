# Created by pyp2rpm-3.3.2
%global pypi_name mock

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Rolling backport of unittest.mock for all Pythons

License:        None
URL:            https://github.com/testing-cabal/mock
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(pbr) >= 1.3
BuildRequires:  python2dist(setuptools)
BuildRequires:  python2dist(setuptools) >= 17.1
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) >= 1.3
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools) >= 17.1
BuildRequires:  python3dist(sphinx)

%description
mock is a library for testing in Python. It allows you to replace parts of your
system under test with mock objects and make assertions about how they have
been used.mock is now part of the Python standard library, available as
unittest.mock < in Python 3.3 This package contains a rolling backport of the
standard library mock code compatible with Python 2.6 and up, and 3.3 and
up.Please see...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(funcsigs) >= 1
Requires:       python2dist(jinja2) < 2.7
Requires:       python2dist(pbr) >= 0.11
Requires:       python2dist(pygments) < 2
Requires:       python2dist(six) >= 1.9
Requires:       python2dist(sphinx)
Requires:       python2dist(sphinx) < 1.3
Requires:       python2dist(unittest2) >= 1.1.0
%description -n python2-%{pypi_name}
mock is a library for testing in Python. It allows you to replace parts of your
system under test with mock objects and make assertions about how they have
been used.mock is now part of the Python standard library, available as
unittest.mock < in Python 3.3 This package contains a rolling backport of the
standard library mock code compatible with Python 2.6 and up, and 3.3 and
up.Please see...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(funcsigs) >= 1
Requires:       python3dist(jinja2) < 2.7
Requires:       python3dist(pbr) >= 0.11
Requires:       python3dist(pygments) < 2
Requires:       python3dist(six) >= 1.9
Requires:       python3dist(sphinx)
Requires:       python3dist(sphinx) < 1.3
Requires:       python3dist(unittest2) >= 1.1.0
%description -n python3-%{pypi_name}
mock is a library for testing in Python. It allows you to replace parts of your
system under test with mock objects and make assertions about how they have
been used.mock is now part of the Python standard library, available as
unittest.mock < in Python 3.3 This package contains a rolling backport of the
standard library mock code compatible with Python 2.6 and up, and 3.3 and
up.Please see...

%package -n python-%{pypi_name}-doc
Summary:        mock documentation
%description -n python-%{pypi_name}-doc
Documentation for mock

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
%py3_install

%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
* Tue Feb 25 2020 mockbuilder - 2.0.0-1
- Initial package.