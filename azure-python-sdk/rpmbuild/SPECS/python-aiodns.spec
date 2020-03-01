# Created by pyp2rpm-3.3.2
%global pypi_name aiodns

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Simple DNS resolver for asyncio

License:        None
URL:            http://github.com/saghul/aiodns
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Simple DNS resolver for asyncio aiodns provides a simple way for doing
asynchronous DNS resolutions using pycares < import asyncio import aiodns loop
asyncio.get_event_loop() resolver aiodns.DNSResolver(looploop) async def
query(name, query_type): return await resolver.query(name, query_type) coro
query('google.com', 'A') result loop.run_until_complete(coro)

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       python3dist(%{pypi_name}) = %{version}
 
Requires:       python3dist(pycares) >= 3.0.0
Requires:       python3dist(typing)
%description -n python3-%{pypi_name}
 Simple DNS resolver for asyncio aiodns provides a simple way for doing
asynchronous DNS resolutions using pycares < import asyncio import aiodns loop
asyncio.get_event_loop() resolver aiodns.DNSResolver(looploop) async def
query(name, query_type): return await resolver.query(name, query_type) coro
query('google.com', 'A') result loop.run_until_complete(coro)


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
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sun Mar 01 2020 Brandon Perkins <bperkins@redhat.com> - 2.0.0-1
- Initial package.