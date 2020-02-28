# Created by pyp2rpm-3.3.2
%global pypi_name Jinja2

Name:           python-%{pypi_name}
Version:        2.11.1
Release:        1%{?dist}
Summary:        A very fast and expressive template engine

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/jinja/
Source0:        https://files.pythonhosted.org/packages/source/J/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(babel) >= 0.8
BuildRequires:  python2dist(markupsafe) >= 0.23
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(babel) >= 0.8
BuildRequires:  python3dist(markupsafe) >= 0.23
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Jinja is a fast, expressive, extensible templating engine. Special placeholders
in the template allow writing code similar to Python syntax. Then the template
is passed data to render the final document.It includes:- Template inheritance
and inclusion. - Define and import macros within templates. - HTML templates
can use autoescaping to prevent XSS from untrusted user input. - A sandboxed...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(babel) >= 0.8
Requires:       python2dist(markupsafe) >= 0.23
Requires:       python2dist(setuptools)
%description -n python2-%{pypi_name}
Jinja is a fast, expressive, extensible templating engine. Special placeholders
in the template allow writing code similar to Python syntax. Then the template
is passed data to render the final document.It includes:- Template inheritance
and inclusion. - Define and import macros within templates. - HTML templates
can use autoescaping to prevent XSS from untrusted user input. - A sandboxed...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(babel) >= 0.8
Requires:       python3dist(markupsafe) >= 0.23
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
Jinja is a fast, expressive, extensible templating engine. Special placeholders
in the template allow writing code similar to Python syntax. Then the template
is passed data to render the final document.It includes:- Template inheritance
and inclusion. - Define and import macros within templates. - HTML templates
can use autoescaping to prevent XSS from untrusted user input. - A sandboxed...

%package -n python-%{pypi_name}-doc
Summary:        Jinja2 documentation
%description -n python-%{pypi_name}-doc
Documentation for Jinja2

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

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE.rst
%doc README.rst
%{python2_sitelib}/jinja2
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/jinja2
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.rst

%changelog
* Tue Feb 25 2020 mockbuilder - 2.11.1-1
- Initial package.