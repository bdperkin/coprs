# Created by pyp2rpm-3.3.4
%global pypi_name google-auth-httplib2

Name:           python-%{pypi_name}
Version:        0.0.4
Release:        1%{?dist}
Summary:        Google Authentication Library: httplib2 transport

License:        Apache 2.0
URL:            https://github.com/GoogleCloudPlatform/google-auth-library-python-httplib2
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(google-auth)
BuildRequires:  python3dist(httplib2) >= 0.9.1
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)

%description
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
Requires:       python3dist(six)
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
%py3_build

%install
%py3_install

%check

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/google_auth_httplib2.py
%{python3_sitelib}/google_auth_httplib2-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Oct 19 2020 Brandon Perkins <bperkins@redhat.com> - 0.0.4-1
- Initial package.
