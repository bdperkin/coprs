# Generated by go2rpm 1
%bcond_with check

# https://github.com/aliyun/aliyun-oss-go-sdk
%global goipath         github.com/aliyun/aliyun-oss-go-sdk
Version:                2.0.4

%gometa

%global common_description %{expand:
Aliyun OSS SDK for Go.}

%global godocs          CHANGELOG.md README.md README-CN.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Aliyun OSS SDK for Go

License:        # FIXME

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/time/rate)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/baiyubin/aliyun-sts-go-sdk/sts)
BuildRequires:  golang(gopkg.in/check.v1)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/aliyun-oss-go-sdk %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%doc CHANGELOG.md README.md README-CN.md
%{_bindir}/*

%gopkgfiles

%changelog
* Fri Nov 22 18:02:03 UTC 2019 Brandon Perkins <bdperkin@gmail.com> - 2.0.4-1
- Initial package

