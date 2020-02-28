# Created by pyp2rpm-3.3.2
%global pypi_name vsts

Name:           python-%{pypi_name}
Version:        0.1.25
Release:        1%{?dist}
Summary:        Python wrapper around the VSTS APIs

License:        MIT
URL:            https://github.com/Microsoft/vsts-python-api
Source0:        https://files.pythonhosted.org/packages/source/v/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(msrest) < 0.7.0
BuildRequires:  python2dist(msrest) >= 0.6.0
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(msrest) < 0.7.0
BuildRequires:  python3dist(msrest) >= 0.6.0
BuildRequires:  python3dist(setuptools)

%description


%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(msrest) < 0.7.0
Requires:       python2dist(msrest) >= 0.6.0
%description -n python2-%{pypi_name}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(msrest) < 0.7.0
Requires:       python3dist(msrest) >= 0.6.0
%description -n python3-%{pypi_name}



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
%license LICENSE.txt vsts/licensing/v4_0/models/account_license_extension_usage.py vsts/licensing/v4_0/models/account_license_usage.py vsts/licensing/v4_0/models/account_user_license.py vsts/licensing/v4_0/models/extension_license_data.py vsts/licensing/v4_0/models/license.py vsts/licensing/v4_1/models/account_license_extension_usage.py vsts/licensing/v4_1/models/account_license_usage.py vsts/licensing/v4_1/models/account_user_license.py vsts/licensing/v4_1/models/extension_license_data.py vsts/licensing/v4_1/models/license.py vsts/maven/v4_1/models/maven_pom_license.py vsts/member_entitlement_management/v4_1/models/license_summary_data.py vsts/task_agent/v4_0/models/task_hub_license_details.py vsts/task_agent/v4_1/models/task_hub_license_details.py
%doc vsts/contributions/v4_0/models/extension_licensing.py vsts/contributions/v4_0/models/licensing_override.py vsts/contributions/v4_1/models/extension_licensing.py vsts/contributions/v4_1/models/licensing_override.py vsts/extension_management/v4_0/models/extension_licensing.py vsts/extension_management/v4_0/models/licensing_override.py vsts/extension_management/v4_1/models/extension_licensing.py vsts/extension_management/v4_1/models/licensing_override.py vsts/licensing/v4_0/licensing_client.py vsts/licensing/v4_1/licensing_client.py
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.txt vsts/licensing/v4_0/models/account_license_extension_usage.py vsts/licensing/v4_0/models/account_license_usage.py vsts/licensing/v4_0/models/account_user_license.py vsts/licensing/v4_0/models/extension_license_data.py vsts/licensing/v4_0/models/license.py vsts/licensing/v4_1/models/account_license_extension_usage.py vsts/licensing/v4_1/models/account_license_usage.py vsts/licensing/v4_1/models/account_user_license.py vsts/licensing/v4_1/models/extension_license_data.py vsts/licensing/v4_1/models/license.py vsts/maven/v4_1/models/maven_pom_license.py vsts/member_entitlement_management/v4_1/models/license_summary_data.py vsts/task_agent/v4_0/models/task_hub_license_details.py vsts/task_agent/v4_1/models/task_hub_license_details.py
%doc vsts/contributions/v4_0/models/extension_licensing.py vsts/contributions/v4_0/models/licensing_override.py vsts/contributions/v4_1/models/extension_licensing.py vsts/contributions/v4_1/models/licensing_override.py vsts/extension_management/v4_0/models/extension_licensing.py vsts/extension_management/v4_0/models/licensing_override.py vsts/extension_management/v4_1/models/extension_licensing.py vsts/extension_management/v4_1/models/licensing_override.py vsts/licensing/v4_0/licensing_client.py vsts/licensing/v4_1/licensing_client.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Feb 25 2020 mockbuilder - 0.1.25-1
- Initial package.