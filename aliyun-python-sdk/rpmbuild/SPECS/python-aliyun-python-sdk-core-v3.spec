# Created by pyp2rpm-3.3.2
%global pypi_name aliyun-python-sdk-core-v3

Name:           python-%{pypi_name}
Version:        2.13.11
Release:        1%{?dist}
Summary:        The core module of Aliyun Python SDK

License:        Apache License 2.0
URL:            https://github.com/aliyun/aliyun-openapi-python-sdk
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 aliyun-python-sdk-core This is the core module of Aliyun Python SDK.Aliyun
Python SDK is the official software development kit. It makes things easy to
integrate your Python application, library, or script with Aliyun services.This
module works on Python versions: * 2.6.5 and greater Documentation:Please visit

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(jmespath) < 1.0.0
Requires:       python2dist(jmespath) >= 0.9.3
Requires:       python2dist(pycryptodome) >= 3.4.7
%description -n python2-%{pypi_name}
 aliyun-python-sdk-core This is the core module of Aliyun Python SDK.Aliyun
Python SDK is the official software development kit. It makes things easy to
integrate your Python application, library, or script with Aliyun services.This
module works on Python versions: * 2.6.5 and greater Documentation:Please visit

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(jmespath) < 1.0.0
Requires:       python3dist(jmespath) >= 0.9.3
Requires:       python3dist(pycryptodome) >= 3.4.7
%description -n python3-%{pypi_name}
 aliyun-python-sdk-core This is the core module of Aliyun Python SDK.Aliyun
Python SDK is the official software development kit. It makes things easy to
integrate your Python application, library, or script with Aliyun services.This
module works on Python versions: * 2.6.5 and greater Documentation:Please visit


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
%doc README.rst
%{python2_sitelib}/aliyunsdkcore
%{python2_sitelib}/aliyun_python_sdk_core_v3-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/aliyunsdkcore
%{python3_sitelib}/aliyun_python_sdk_core_v3-%{version}-py?.?.egg-info

%changelog
* Thu Feb 20 2020 mockbuilder - 2.13.11-1
- Initial package.