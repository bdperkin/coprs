# Created by pyp2rpm-3.3.2
%global pypi_name google-auth-httplib2

Name:           python-%{pypi_name}
Version:        0.0.3
Release:        1%{?dist}
Summary:        Google Authentication Library: httplib2 transport

License:        Apache 2.0
URL:            https://github.com/GoogleCloudPlatform/google-auth-library-python-httplib2
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(google-auth)
BuildRequires:  python2dist(httplib2) >= 0.9.1
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(google-auth)
BuildRequires:  python3dist(httplib2) >= 0.9.1
BuildRequires:  python3dist(setuptools)

%description
httplib2 Transport for Google Auth |pypi|This library provides an httplib2_
transport for google-auth_... note:: httplib has lots of problems such as lack
of threadsafety and insecure usage of TLS. Using it is highly discouraged. This
library is intended to help existing users of oauth2client migrate to google-
auth... |pyp .. _httplib2: .. _google-auth:

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(google-auth)
Requires:       python2dist(httplib2) >= 0.9.1
%description -n python2-%{pypi_name}
httplib2 Transport for Google Auth |pypi|This library provides an httplib2_
transport for google-auth_... note:: httplib has lots of problems such as lack
of threadsafety and insecure usage of TLS. Using it is highly discouraged. This
library is intended to help existing users of oauth2client migrate to google-
auth... |pyp .. _httplib2: .. _google-auth:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(google-auth)
Requires:       python3dist(httplib2) >= 0.9.1
%description -n python3-%{pypi_name}
httplib2 Transport for Google Auth |pypi|This library provides an httplib2_
transport for google-auth_... note:: httplib has lots of problems such as lack
of threadsafety and insecure usage of TLS. Using it is highly discouraged. This
library is intended to help existing users of oauth2client migrate to google-
auth... |pyp .. _httplib2: .. _google-auth:


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
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/google_auth_httplib2.py*
%{python2_sitelib}/google_auth_httplib2-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/google_auth_httplib2.py
%{python3_sitelib}/google_auth_httplib2-%{version}-py?.?.egg-info

%changelog
* Fri Feb 21 2020 mockbuilder - 0.0.3-1
- Initial package.