# Created by pyp2rpm-3.3.2
%global pypi_name pytest-localserver

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        1%{?dist}
Summary:        py.test plugin to test server connections locally

License:        MIT License
URL:            http://bitbucket.org/pytest-dev/pytest-localserver/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest) >= 2.0.0
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(werkzeug) >= 0.10

%description
 pytest-localserver pytest-localserver is a plugin for the pytest_ testing
framework which enables you to test server connections locally.Sometimes
monkeypatching_ urllib2.urlopen() just does not cut it, for instance if you
work with urllib2.Request, define your own openers/handlers or work with
httplib. In these cases it may come in handy to have an HTTP server running
locally which behaves...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(setuptools)
Requires:       python3dist(werkzeug) >= 0.10
%description -n python3-%{pypi_name}
 pytest-localserver pytest-localserver is a plugin for the pytest_ testing
framework which enables you to test server connections locally.Sometimes
monkeypatching_ urllib2.urlopen() just does not cut it, for instance if you
work with urllib2.Request, define your own openers/handlers or work with
httplib. In these cases it may come in handy to have an HTTP server running
locally which behaves...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/pytest_localserver
%{python3_sitelib}/pytest_localserver-%{version}-py?.?.egg-info

%changelog
* Fri Feb 21 2020 mockbuilder - 0.5.0-1
- Initial package.