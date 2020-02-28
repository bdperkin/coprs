# Created by pyp2rpm-3.3.2
%global pypi_name applicationinsights

Name:           python-%{pypi_name}
Version:        0.11.9
Release:        1%{?dist}
Summary:        This project extends the Application Insights API surface to support Python

License:        MIT
URL:            https://github.com/Microsoft/ApplicationInsights-Python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Application Insights for Python This project extends the Application Insights
API surface to support Python. Application Insights < is a service that allows
developers to keep their application available, performing and succeeding. This
Python module will allow you to send telemetry of various kinds

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Application Insights for Python This project extends the Application Insights
API surface to support Python. Application Insights < is a service that allows
developers to keep their application available, performing and succeeding. This
Python module will allow you to send telemetry of various kinds

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Application Insights for Python This project extends the Application Insights
API surface to support Python. Application Insights < is a service that allows
developers to keep their application available, performing and succeeding. This
Python module will allow you to send telemetry of various kinds


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
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Feb 25 2020 mockbuilder - 0.11.9-1
- Initial package.