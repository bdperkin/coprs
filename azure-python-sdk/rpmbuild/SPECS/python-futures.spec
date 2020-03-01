# Created by pyp2rpm-3.3.2
%global pypi_name futures

Name:           python-%{pypi_name}
Version:        3.1.1
Release:        1%{?dist}
Summary:        Backport of the concurrent.futures package from Python 3

License:        PSF
URL:            https://github.com/agronholm/pythonfutures
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
UNKNOWN

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}

%description -n python3-%{pypi_name}
UNKNOWN

%package -n python-%{pypi_name}-doc
Summary:        futures documentation
%description -n python-%{pypi_name}-doc
Documentation for futures

%prep
%autosetup -n %{pypi_name}-%{version}
# Fix compatible release specifiers
sed -i -e 's/~=/>=/g' setup.py
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test || true

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/concurrent
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 3.1.1-1
- Initial package.