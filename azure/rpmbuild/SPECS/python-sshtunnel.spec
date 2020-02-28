# Created by pyp2rpm-3.3.2
%global pypi_name sshtunnel

Name:           python-%{pypi_name}
Version:        0.1.5
Release:        1%{?dist}
Summary:        Pure python SSH tunnels

License:        MIT
URL:            https://github.com/pahaz/sshtunnel
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(check-manifest)
BuildRequires:  python2dist(paramiko) >= 1.15.2
BuildRequires:  python2dist(setuptools)
BuildRequires:  python2dist(tox) >= 1.8.1
BuildRequires:  python2dist(tox) >= 1.8.1
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(check-manifest)
BuildRequires:  python3dist(paramiko) >= 1.15.2
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinxcontrib-napoleon)
BuildRequires:  python3dist(tox) >= 1.8.1
BuildRequires:  python3dist(tox) >= 1.8.1
BuildRequires:  python3dist(sphinx)

%description
|CircleCI| |AppVeyor| |readthedocs| |coveralls| |version||pyversions|
|license|**Author**: Pahaz Blinov_**Repo**: by but it doesn't work on See also:
-* paramiko_Installation sshtunnel_ is on PyPI, so simply run::: pip install
sshtunnelor :: easy_install sshtunnelor :: conda install -c conda-forge
sshtunnelto have it installed in your environment.For installing from source,
clone the repo < and run::

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(paramiko) >= 1.15.2
Requires:       python2dist(setuptools)
Requires:       python2dist(sphinx)
Requires:       python2dist(sphinxcontrib-napoleon)
Requires:       python2dist(tox) >= 1.8.1
%description -n python2-%{pypi_name}
|CircleCI| |AppVeyor| |readthedocs| |coveralls| |version||pyversions|
|license|**Author**: Pahaz Blinov_**Repo**: by but it doesn't work on See also:
-* paramiko_Installation sshtunnel_ is on PyPI, so simply run::: pip install
sshtunnelor :: easy_install sshtunnelor :: conda install -c conda-forge
sshtunnelto have it installed in your environment.For installing from source,
clone the repo < and run::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(paramiko) >= 1.15.2
Requires:       python3dist(setuptools)
Requires:       python3dist(sphinx)
Requires:       python3dist(sphinxcontrib-napoleon)
Requires:       python3dist(tox) >= 1.8.1
%description -n python3-%{pypi_name}
|CircleCI| |AppVeyor| |readthedocs| |coveralls| |version||pyversions|
|license|**Author**: Pahaz Blinov_**Repo**: by but it doesn't work on See also:
-* paramiko_Installation sshtunnel_ is on PyPI, so simply run::: pip install
sshtunnelor :: easy_install sshtunnelor :: conda install -c conda-forge
sshtunnelto have it installed in your environment.For installing from source,
clone the repo < and run::

%package -n python-%{pypi_name}-doc
Summary:        sshtunnel documentation
%description -n python-%{pypi_name}-doc
Documentation for sshtunnel

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
rm -rf %{buildroot}%{_bindir}/*
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/sshtunnel
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Feb 25 2020 mockbuilder - 0.1.5-1
- Initial package.