# Created by pyp2rpm-3.3.2
%global pypi_name uamqp

Name:           python-%{pypi_name}
Version:        1.2.6
Release:        2%{?dist}
Summary:        AMQP 1.0 Client Library for Python

License:        MIT License
URL:            https://github.com/Azure/azure-uamqp-python
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
uAMQP for Python An AMQP 1.0 client library for Python. Installation Wheels are
provided for most major operating systems, so you can install directly with
pip:.. code:: shell $ pip install uamqp

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(certifi) >= 2017.4.17
Requires:       python3dist(six) >= 1.0
%description -n python3-%{pypi_name}
uAMQP for Python An AMQP 1.0 client library for Python. Installation Wheels are
provided for most major operating systems, so you can install directly with
pip:.. code:: shell $ pip install uamqp


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

%files -n python3-%{pypi_name}
%license src/vendor/azure-uamqp-c/LICENSE src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/LICENSE src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/testtools/ctest/LICENSE
%doc README.rst src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/README.md src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/adapters/README.md src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/archive/cyclonessl/readme.md src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/devdoc/img/readme.txt src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/devdoc/img_src/readme.txt src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/pal/README.md src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/src/README.md src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/tests/dns_async_ut/win32_fake_linux/readme.txt src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/tests/socket_async_ut/win32_fake_linux/readme.txt src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/testtools/ctest/README.md src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/testtools/testrunner/readme.md src/vendor/azure-uamqp-c/deps/azure-c-shared-utility/testtools/umock-c/readme.md src/vendor/azure-uamqp-c/readme.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.6-2
- Rebuilt.

* Wed Mar 11 2020 Brandon Perkins <bperkins@redhat.com> - 1.2.6-1
- Initial package.