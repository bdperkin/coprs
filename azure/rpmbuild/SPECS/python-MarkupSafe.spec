# Created by pyp2rpm-3.3.2
%global pypi_name MarkupSafe

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        1%{?dist}
Summary:        Safely add untrusted strings to HTML/XML markup

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/markupsafe/
Source0:        https://files.pythonhosted.org/packages/source/M/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
MarkupSafe MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are replaced
so that they display as the actual characters. This mitigates injection
attacks, meaning untrusted user input can safely be displayed on a page.
Installing -Install and update using pip_:.. code-block:: text pip install -U
MarkupSafe.....

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
MarkupSafe MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are replaced
so that they display as the actual characters. This mitigates injection
attacks, meaning untrusted user input can safely be displayed on a page.
Installing -Install and update using pip_:.. code-block:: text pip install -U
MarkupSafe.....

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
MarkupSafe MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are replaced
so that they display as the actual characters. This mitigates injection
attacks, meaning untrusted user input can safely be displayed on a page.
Installing -Install and update using pip_:.. code-block:: text pip install -U
MarkupSafe.....

%package -n python-%{pypi_name}-doc
Summary:        MarkupSafe documentation
%description -n python-%{pypi_name}-doc
Documentation for MarkupSafe

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
%license LICENSE.rst docs/license.rst
%doc README.rst
%{python2_sitearch}/markupsafe
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.rst docs/license.rst
%doc README.rst
%{python3_sitearch}/markupsafe
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.rst docs/license.rst

%changelog
* Tue Feb 25 2020 mockbuilder - 1.1.1-1
- Initial package.