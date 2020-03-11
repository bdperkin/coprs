# Created by pyp2rpm-3.3.2
%global pypi_name azure-mgmt-storage

Name:           python-%{pypi_name}
Version:        8.0.0
Release:        1%{?dist}
Summary:        Microsoft Azure Storage Management Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(azure-common) >= 1.1
BuildRequires:  python3dist(azure-mgmt-nspkg)
BuildRequires:  python3dist(msrest) >= 0.5.0
BuildRequires:  python3dist(msrestazure) < 2.0.0
BuildRequires:  python3dist(msrestazure) >= 0.4.32
BuildRequires:  python3dist(setuptools)

%description
 Microsoft Azure SDK for PythonThis is the Microsoft Azure Storage Management
Client Library. This package has been tested with Python 2.7, 3.5, 3.6, 3.7 and
3.8. For a more complete view of Azure libraries, see the [Github repo]( For
code examples, see [Storage Management]( on docs.microsoft.com. Provide
FeedbackIf you encounter any bugs or have suggestions, please file an issue in
the...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-common) >= 1.1
Requires:       python3dist(azure-mgmt-nspkg)
Requires:       python3dist(msrest) >= 0.5.0
Requires:       python3dist(msrestazure) < 2.0.0
Requires:       python3dist(msrestazure) >= 0.4.32
%description -n python3-%{pypi_name}
 Microsoft Azure SDK for PythonThis is the Microsoft Azure Storage Management
Client Library. This package has been tested with Python 2.7, 3.5, 3.6, 3.7 and
3.8. For a more complete view of Azure libraries, see the [Github repo]( For
code examples, see [Storage Management]( on docs.microsoft.com. Provide
FeedbackIf you encounter any bugs or have suggestions, please file an issue in
the...


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
%doc README.md
%{python3_sitelib}/azure
%{python3_sitelib}/azure_mgmt_storage-%{version}-py?.?.egg-info

%changelog
* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 8.0.0-1
- Upgrade to version 8.0.0.

* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 7.2.0-1
- Initial package.