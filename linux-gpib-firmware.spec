%global fwdate 2008-08-10

%global fwdir %{_prefix}/lib/firmware

%global agilent_loader_a linux-gpib-firmware-loader-agilent82357a@ 
%global agilent_loader_b linux-gpib-firmware-loader-agilent82357b@ 
%global ni_loader linux-gpib-firmware-loader-ni@ 

Name:           linux-gpib-firmware
Version:        %(echo %{fwdate} | tr -d -)
Release:        1%{?dist}
Summary:        Firmware for GPIB (IEEE-488) adapters
BuildArch:      noarch

License:        Unknown
URL:            http://linux-gpib.sourceforge.io/

Source0:        https://linux-gpib.sourceforge.io/firmware/gpib_firmware-%{fwdate}.tar.gz
Source1:        %{agilent_loader_a}.service.in
Source2:        %{agilent_loader_b}.service.in
Source3:        %{ni_loader}.service.in
Source4:        61-%{name}.rules

%{?systemd_requires}
Requires:       linux-gpib dkms-linux-gpib
Requires:       fxload
BuildRequires:  systemd
BuildRequires:  sed

%description
Firmware for GPIB (IEEE-488) adapters.

This package contains firmware for:
    - NI GPIB-USB-B
    - HP/Agilent/Keysight:
        - 82357A
        - 82341C
        - 82341D
        - 82350A
        - 82357A
        - 82357B


%prep
%setup -q -n gpib_firmware-%{fwdate}


%install
shopt -s nullglob

for adapter in agilent_82357a hp_82341 hp_82350a ni_gpib_usb_b ; do
    install -d %{buildroot}%{fwdir}/$adapter
    install -p -m 0644 $adapter/{*.bin,*.hex} %{buildroot}%{fwdir}/$adapter
    test -e $adapter/README && cp -fp $adapter/README README.$adapter
done

install -d %{buildroot}%{_unitdir}
sed -e 's|@fwdir@|%{fwdir}|g' %{SOURCE1} > %{agilent_loader_a}.service
install -p -m 0644 %{agilent_loader_a}.service %{buildroot}%{_unitdir}
sed -e 's|@fwdir@|%{fwdir}|g' %{SOURCE2} > %{agilent_loader_b}.service
install -p -m 0644 %{agilent_loader_b}.service %{buildroot}%{_unitdir}
sed -e 's|@fwdir@|%{fwdir}|g' %{SOURCE3} > %{ni_loader}.service
install -p -m 0644 %{ni_loader}.service %{buildroot}%{_unitdir}

install -d %{buildroot}%{_udevrulesdir}
install -p -m 0644 %{SOURCE4} %{buildroot}%{_udevrulesdir}

%build
# empty

%post
udevadm control --reload > /dev/null 2>&1 || :
%systemd_post %{agilent_loader_a}.service
%systemd_post %{agilent_loader_b}.service
%systemd_post %{ni_loader}.service


%preun
%systemd_preun %{agilent_loader_a}.service
%systemd_preun %{agilent_loader_b}.service
%systemd_preun %{ni_loader}.service
udevadm control --reload > /dev/null 2>&1 || :


%postun
%systemd_postun %{agilent_loader_a}.service
%systemd_postun %{agilent_loader_b}.service
%systemd_postun %{ni_loader}.service
udevadm control --reload > /dev/null 2>&1 || :


%files
%defattr(644,root,root,755)

%doc README*

%dir %{fwdir}/agilent_82357a
%dir %{fwdir}/hp_82341
%dir %{fwdir}/hp_82350a
%dir %{fwdir}/ni_gpib_usb_b

%{fwdir}/agilent_82357a/*.hex
%{fwdir}/hp_82341/*.bin
%{fwdir}/hp_82350a/*.bin
%{fwdir}/ni_gpib_usb_b/*.hex

%{_unitdir}/*.service

%{_udevrulesdir}/*.rules

%changelog
* Sat Jun 16 2018 Colin Samples <colin-dot-samples-at-gmail-dot-com> - 20080810-1
- Initial release
