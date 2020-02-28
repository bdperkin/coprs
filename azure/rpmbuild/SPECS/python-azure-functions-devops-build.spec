# Created by pyp2rpm-3.3.2
%global pypi_name azure-functions-devops-build

Name:           python-%{pypi_name}
Version:        0.0.22
Release:        1%{?dist}
Summary:        Python package for integrating Azure Functions with Azure DevOps

License:        MIT
URL:            https://github.com/Azure/azure-functions-devops-build
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Azure Devops Build Manager For Azure Functions> :construction: The project is
currently **work in progress**. Please **do not use in production** as we
expect developments over time. :construction:This project provides the class
AzureDevopsBuildManager and supporting classes. This manager class allows the
caller to manage Azure Devops pipelines that are maintained within an Azure
Devops...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(jinja2)
Requires:       python2dist(msrest)
Requires:       python2dist(vsts)
%description -n python2-%{pypi_name}
 Azure Devops Build Manager For Azure Functions> :construction: The project is
currently **work in progress**. Please **do not use in production** as we
expect developments over time. :construction:This project provides the class
AzureDevopsBuildManager and supporting classes. This manager class allows the
caller to manage Azure Devops pipelines that are maintained within an Azure
Devops...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(jinja2)
Requires:       python3dist(msrest)
Requires:       python3dist(vsts)
%description -n python3-%{pypi_name}
 Azure Devops Build Manager For Azure Functions> :construction: The project is
currently **work in progress**. Please **do not use in production** as we
expect developments over time. :construction:This project provides the class
AzureDevopsBuildManager and supporting classes. This manager class allows the
caller to manage Azure Devops pipelines that are maintained within an Azure
Devops...


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

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.md
%{python2_sitelib}/azure_functions_devops_build
%{python2_sitelib}/azure_functions_devops_build-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/azure_functions_devops_build
%{python3_sitelib}/azure_functions_devops_build-%{version}-py?.?.egg-info

%changelog
* Tue Feb 25 2020 mockbuilder - 0.0.22-1
- Initial package.