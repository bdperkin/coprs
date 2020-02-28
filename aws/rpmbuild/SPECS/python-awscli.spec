# Created by pyp2rpm-3.3.2
%global pypi_name awscli

Name:           python-%{pypi_name}
Version:        1.18.7
Release:        1%{?dist}
Summary:        Universal Command Line Environment for AWS

License:        Apache License 2.0
URL:            http://aws.amazon.com/cli/
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
aws-cli This package provides a unified command line interface to Amazon Web
Services.The aws-cli package works on Python versions:* 2.7.x and greater *
3.4.x and greater * 3.5.x and greater * 3.6.x and greater * 3.7.x and greater *
3.8.x and greaterOn 10/09/2019 support for Python 2.6 and Python 3.3 was
deprecated and support was dropped on 01/10/2020. To avoid disruption,
customers using the AWS CLI

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(botocore) = 1.15.7
Requires:       python2dist(colorama) < 0.4.4
Requires:       python2dist(colorama) >= 0.2.5
Requires:       python2dist(docutils) < 0.16
Requires:       python2dist(docutils) >= 0.10
Requires:       python2dist(pyyaml) < 5.3
Requires:       python2dist(pyyaml) >= 3.10
Requires:       python2dist(rsa) <= 3.5.0
Requires:       python2dist(rsa) >= 3.1.2
Requires:       python2dist(s3transfer) < 0.4.0
Requires:       python2dist(s3transfer) >= 0.3.0
%description -n python2-%{pypi_name}
aws-cli This package provides a unified command line interface to Amazon Web
Services.The aws-cli package works on Python versions:* 2.7.x and greater *
3.4.x and greater * 3.5.x and greater * 3.6.x and greater * 3.7.x and greater *
3.8.x and greaterOn 10/09/2019 support for Python 2.6 and Python 3.3 was
deprecated and support was dropped on 01/10/2020. To avoid disruption,
customers using the AWS CLI

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(botocore) = 1.15.7
Requires:       python3dist(colorama) < 0.4.4
Requires:       python3dist(colorama) >= 0.2.5
Requires:       python3dist(docutils) < 0.16
Requires:       python3dist(docutils) >= 0.10
Requires:       python3dist(pyyaml) < 5.3
Requires:       python3dist(pyyaml) >= 3.10
Requires:       python3dist(rsa) <= 3.5.0
Requires:       python3dist(rsa) >= 3.1.2
Requires:       python3dist(s3transfer) < 0.4.0
Requires:       python3dist(s3transfer) >= 0.3.0
%description -n python3-%{pypi_name}
aws-cli This package provides a unified command line interface to Amazon Web
Services.The aws-cli package works on Python versions:* 2.7.x and greater *
3.4.x and greater * 3.5.x and greater * 3.6.x and greater * 3.7.x and greater *
3.8.x and greaterOn 10/09/2019 support for Python 2.6 and Python 3.3 was
deprecated and support was dropped on 01/10/2020. To avoid disruption,
customers using the AWS CLI


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
rm -rf %{buildroot}%{_bindir}/*
%py3_install

%files -n python2-%{pypi_name}
%license LICENSE.txt awscli/examples/license-manager/get-license-configuration.rst awscli/examples/license-manager/list-usage-for-license-configuration.rst awscli/examples/license-manager/list-license-configurations.rst awscli/examples/license-manager/update-license-specifications-for-resource.rst awscli/examples/license-manager/list-associations-for-license-configuration.rst awscli/examples/license-manager/delete-license-configuration.rst awscli/examples/license-manager/update-license-configuration.rst awscli/examples/license-manager/create-license-configuration.rst awscli/examples/license-manager/list-license-specifications-for-resource.rst
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.txt awscli/examples/license-manager/get-license-configuration.rst awscli/examples/license-manager/list-usage-for-license-configuration.rst awscli/examples/license-manager/list-license-configurations.rst awscli/examples/license-manager/update-license-specifications-for-resource.rst awscli/examples/license-manager/list-associations-for-license-configuration.rst awscli/examples/license-manager/delete-license-configuration.rst awscli/examples/license-manager/update-license-configuration.rst awscli/examples/license-manager/create-license-configuration.rst awscli/examples/license-manager/list-license-specifications-for-resource.rst
%doc README.rst
%{_bindir}/aws
%{_bindir}/aws.cmd
%{_bindir}/aws_bash_completer
%{_bindir}/aws_completer
%{_bindir}/aws_zsh_completer.sh
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Feb 26 2020 mockbuilder - 1.18.7-1
- Initial package.