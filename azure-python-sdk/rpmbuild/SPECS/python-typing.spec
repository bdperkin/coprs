# Created by pyp2rpm-3.3.2
%global pypi_name typing

Name:           python-%{pypi_name}
Version:        3.7.4.1
Release:        1%{?dist}
Summary:        Type Hints for Python

License:        PSF
URL:            https://docs.python.org/3/library/typing.html
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Typing -- Type Hints for PythonThis is a backport of the standard library
typing module to Python versions older than 3.5. (See note below for newer
versions.)Typing defines a standard notation for Python function and variable
type annotations. The notation can be used for documenting code in a concise,
standard format, and it has been designed to also be used by static and runtime
type...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}

%description -n python3-%{pypi_name}
Typing -- Type Hints for PythonThis is a backport of the standard library
typing module to Python versions older than 3.5. (See note below for newer
versions.)Typing defines a standard notation for Python function and variable
type annotations. The notation can be used for documenting code in a concise,
standard format, and it has been designed to also be used by static and runtime
type...


%prep
%autosetup -n %{pypi_name}-%{version}
# Fix compatible release specifiers
sed -i -e 's/~=/>=/g' setup.py
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test || true

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 3.7.4.1-1
- Initial package.