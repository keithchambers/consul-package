%define debug_package %{nil}

Name:           consul
Version:        0.4.0
Release:        1%{?dist}
Summary:        Consul is a tool for service discovery and configuration.
License:        MPLv2.0
URL:            http://www.consul.io
Source0:        https://dl.bintray.com/mitchellh/consul/%{version}_linux_amd64.zip
Source1:        %{name}.sysconfig
Source2:        %{name}.service
BuildArch:      x86_64
BuildRequires:  systemd-units
Requires:       systemd
requires:       shadow-utils

%description
A distributed, highly available, and extremely scalable tool for service
discovery and configuration.

%prep
%setup -c -n %{version}_linux_amd64

%build

%install
install -m0755 -d %{buildroot}/%{_bindir}
install -m0755 -d %{buildroot}/%{_sysconfdir}/%{name}.d
install -m0755 -d %{buildroot}/%{_sysconfdir}/sysconfig
install -m0755 -d %{buildroot}/%{_sharedstatedir}/%{name}
install -m0755 -d %{buildroot}/%{_unitdir}
install -m0755 %{name} %{buildroot}/%{_bindir}
install -m0644 %{_sourcedir}/%{name}.sysconfig %{buildroot}/%{_sysconfdir}/sysconfig/%{name}
install -m0644 %{_sourcedir}/%{name}.service %{buildroot}/%{_unitdir}

%pre
getent group  %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || useradd -r -g %{name} -s /sbin/nologin -c "%{name} daemon" %{name}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
userdel  %{name}
groupdel %{name}

%files
%{_bindir}/%{name}
%{_sysconfdir}/%{name}.d
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(0750,%{name},%{name}) %{_sharedstatedir}/%{name}

%changelog
* %(date "+%a %b %d %Y") %{name} - %{version}-%{release}
- build %{name} - %{version}-%{release}
