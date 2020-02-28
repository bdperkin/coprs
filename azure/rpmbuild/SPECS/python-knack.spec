# Created by pyp2rpm-3.3.2
%global pypi_name knack

Name:           python-%{pypi_name}
Version:        0.6.3
Release:        1%{?dist}
Summary:        A Command-Line Interface framework

License:        MIT
URL:            https://github.com/microsoft/knack
Source0:        https://files.pythonhosted.org/packages/source/k/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(argcomplete)
BuildRequires:  python2dist(colorama)
BuildRequires:  python2dist(enum34)
BuildRequires:  python2dist(jmespath)
BuildRequires:  python2dist(pygments)
BuildRequires:  python2dist(pyyaml)
BuildRequires:  python2dist(setuptools)
BuildRequires:  python2dist(six)
BuildRequires:  python2dist(tabulate)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(argcomplete)
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(enum34)
BuildRequires:  python3dist(jmespath)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(tabulate)

%description
 _ _ | | ___ __ __ _ ___| | __ | |/ / '_ \ / _ |/ __| |/ / | <| | | | (_| |
(__| < |_|\_\_| |_|\__,_|\___|_|\_\ **A Command-Line Interface
framework**Installation is easy via pip:.. code-block:: bash pip install
knackKnack can be installed as a non-privileged user to your home directory by
adding "--user" as below:

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(argcomplete)
Requires:       python2dist(colorama)
Requires:       python2dist(enum34)
Requires:       python2dist(jmespath)
Requires:       python2dist(pygments)
Requires:       python2dist(pyyaml)
Requires:       python2dist(six)
Requires:       python2dist(tabulate)
%description -n python2-%{pypi_name}
 _ _ | | ___ __ __ _ ___| | __ | |/ / '_ \ / _ |/ __| |/ / | <| | | | (_| |
(__| < |_|\_\_| |_|\__,_|\___|_|\_\ **A Command-Line Interface
framework**Installation is easy via pip:.. code-block:: bash pip install
knackKnack can be installed as a non-privileged user to your home directory by
adding "--user" as below:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(argcomplete)
Requires:       python3dist(colorama)
Requires:       python3dist(enum34)
Requires:       python3dist(jmespath)
Requires:       python3dist(pygments)
Requires:       python3dist(pyyaml)
Requires:       python3dist(six)
Requires:       python3dist(tabulate)
%description -n python3-%{pypi_name}
 _ _ | | ___ __ __ _ ___| | __ | |/ / '_ \ / _ |/ __| |/ / | <| | | | (_| |
(__| < |_|\_\_| |_|\__,_|\___|_|\_\ **A Command-Line Interface
framework**Installation is easy via pip:.. code-block:: bash pip install
knackKnack can be installed as a non-privileged user to your home directory by
adding "--user" as below:


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
%doc README.rst tests/README.md
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst tests/README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Feb 25 2020 mockbuilder - 0.6.3-1
- Initial package.