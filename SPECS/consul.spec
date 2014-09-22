Name:           consul
Version:        0.4.0
Release:        1%{?dist}
Summary:        A tool for service discovery and configuration
License:        MPLv2.0
URL:            http://www.consul.io
Source0:        https://dl.bintray.com/mitchellh/consul/%{version}_linux_amd64.zip
Source1:        %{name}.sysconfig
Source2:        %{name}.service
BuildArch:      x86_64
BuildRequires:  systemd-units
Requires:       systemd

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

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_bindir}/%{name}
%{_sysconfdir}/%{name}.d
%{_sharedstatedir}/%{name}
%{_unitdir}/%{name}.service

%changelog
* Sun Sep 14 2014 Keith Chambers - 0.4.0-1
- Initial package spec.
