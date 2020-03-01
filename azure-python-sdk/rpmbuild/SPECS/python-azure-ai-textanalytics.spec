# Created by pyp2rpm-3.3.2
%global pypi_name azure-ai-textanalytics

Name:           python-%{pypi_name}
Version:        1.0.0b2
Release:        1%{?dist}
Summary:        Microsoft Azure Text Analytics Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-sdk-for-python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(azure-ai-nspkg)
BuildRequires:  python3dist(azure-common) >= 1.1
BuildRequires:  python3dist(azure-core) < 2.0.0
BuildRequires:  python3dist(azure-core) >= 1.1.0
BuildRequires:  python3dist(msrest) >= 0.6.0
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.6
BuildRequires:  python3dist(typing)

%description
 Azure Text Analytics client library for Python Text Analytics is a cloud-based
service that provides advanced natural language processing over raw text, and
includes six main functions:* Sentiment Analysis * Named Entity Recognition *
Personally Identifiable Information (PII) Entity Recognition * Linked Entity
Recognition * Language Detection * Key Phrase Extraction[Source code]( |
[Package...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(azure-ai-nspkg)
Requires:       python3dist(azure-common) >= 1.1
Requires:       python3dist(azure-core) < 2.0.0
Requires:       python3dist(azure-core) >= 1.1.0
Requires:       python3dist(msrest) >= 0.6.0
Requires:       python3dist(six) >= 1.6
Requires:       python3dist(typing)
%description -n python3-%{pypi_name}
 Azure Text Analytics client library for Python Text Analytics is a cloud-based
service that provides advanced natural language processing over raw text, and
includes six main functions:* Sentiment Analysis * Named Entity Recognition *
Personally Identifiable Information (PII) Entity Recognition * Linked Entity
Recognition * Language Detection * Key Phrase Extraction[Source code]( |
[Package...


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
%doc README.md samples/README.md
%{python3_sitelib}/azure
%{python3_sitelib}/azure_ai_textanalytics-%{version}-py?.?.egg-info

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 1.0.0b2-1
- Initial package.