# Created by pyp2rpm-3.3.2
%global pypi_name azure-cognitiveservices-language-spellcheck

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Microsoft Azure Cognitive Services Spellcheck Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(azure-cognitiveservices-language-nspkg)
BuildRequires:  python3dist(azure-common) >= 1.1
BuildRequires:  python3dist(msrest) >= 0.5.0
BuildRequires:  python3dist(setuptools)

%description
Microsoft Azure SDK for Python This is the Microsoft Azure Cognitive Services
Spellcheck Client Library.This package has been tested with Python 2.7, 3.5,
3.6, 3.7 and 3.8.For a more complete set of Azure libraries, see the azure <
bundle package.For code examples, see Cognitive Services Spellcheck < on
docs.microsoft.com. Provide Feedback If you encounter any bugs or have
suggestions, please...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-cognitiveservices-language-nspkg)
Requires:       python3dist(azure-common) >= 1.1
Requires:       python3dist(msrest) >= 0.5.0
%description -n python3-%{pypi_name}
Microsoft Azure SDK for Python This is the Microsoft Azure Cognitive Services
Spellcheck Client Library.This package has been tested with Python 2.7, 3.5,
3.6, 3.7 and 3.8.For a more complete set of Azure libraries, see the azure <
bundle package.For code examples, see Cognitive Services Spellcheck < on
docs.microsoft.com. Provide Feedback If you encounter any bugs or have
suggestions, please...


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
%doc README.rst
%{python3_sitelib}/azure
%{python3_sitelib}/azure_cognitiveservices_language_spellcheck-%{version}-py?.?.egg-info

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.0-1
- Initial package.