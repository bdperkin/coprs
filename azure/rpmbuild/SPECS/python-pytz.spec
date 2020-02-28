# Created by pyp2rpm-3.3.2
%global pypi_name pytz

Name:           python-%{pypi_name}
Version:        2019.1
Release:        1%{?dist}
Summary:        World timezone definitions, modern and historical

License:        MIT
URL:            http://pythonhosted.org/pytz
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
pytz - World Timezone Definitions for Python :Author: Stuart Bishop
<stuart@stuartbishop.net>Introduction pytz brings the Olson tz database into
Python. This library allows accurate and cross platform timezone calculations
using Python 2.4 or higher. It also solves the issue of ambiguous times at the
end of daylight saving time, which you can read more about in the Python
Library Reference...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
pytz - World Timezone Definitions for Python :Author: Stuart Bishop
<stuart@stuartbishop.net>Introduction pytz brings the Olson tz database into
Python. This library allows accurate and cross platform timezone calculations
using Python 2.4 or higher. It also solves the issue of ambiguous times at the
end of daylight saving time, which you can read more about in the Python
Library Reference...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pytz - World Timezone Definitions for Python :Author: Stuart Bishop
<stuart@stuartbishop.net>Introduction pytz brings the Olson tz database into
Python. This library allows accurate and cross platform timezone calculations
using Python 2.4 or higher. It also solves the issue of ambiguous times at the
end of daylight saving time, which you can read more about in the Python
Library Reference...


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
%license LICENSE.txt
%doc README.txt
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Feb 25 2020 mockbuilder - 2019.1-1
- Initial package.