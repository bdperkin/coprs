# Created by pyp2rpm-3.3.2
%global pypi_name Pygments

Name:           python-%{pypi_name}
Version:        2.5.2
Release:        1%{?dist}
Summary:        Pygments is a syntax highlighting package written in Python

License:        BSD License
URL:            http://pygments.org/
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Pygments is a syntax highlighting package written in Python.It is a generic
syntax highlighter suitable for use in code hosting, forums, wikis or other
applications that need to prettify source code. Highlights * a wide range of
over 300 languages and other text formats is supported * special attention is
paid to details, increasing quality by a fair amount * support for new
languages and...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(setuptools)
%description -n python2-%{pypi_name}
Pygments is a syntax highlighting package written in Python.It is a generic
syntax highlighter suitable for use in code hosting, forums, wikis or other
applications that need to prettify source code. Highlights * a wide range of
over 300 languages and other text formats is supported * special attention is
paid to details, increasing quality by a fair amount * support for new
languages and...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
Pygments is a syntax highlighting package written in Python.It is a generic
syntax highlighter suitable for use in code hosting, forums, wikis or other
applications that need to prettify source code. Highlights * a wide range of
over 300 languages and other text formats is supported * special attention is
paid to details, increasing quality by a fair amount * support for new
languages and...

%package -n python-%{pypi_name}-doc
Summary:        Pygments documentation
%description -n python-%{pypi_name}-doc
Documentation for Pygments

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 doc html
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
%{python2_sitearch}/pygments
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/pygmentize
%{python3_sitearch}/pygments
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Feb 25 2020 mockbuilder - 2.5.2-1
- Initial package.