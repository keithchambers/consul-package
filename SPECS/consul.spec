%define debug_package %{nil}

name:           consul
version:        0.4.1
release:        1%{?dist}
summary:        Consul is a tool for service discovery and configuration
license:        MPLv2.0
url:            http://www.consul.io
source0:        https://dl.bintray.com/mitchellh/consul/%{version}_linux_amd64.zip
source1:        %{name}.sysconfig
source2:        %{name}.service
buildrequires:  systemd-units
requires:       systemd
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
userdel %{name}
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
