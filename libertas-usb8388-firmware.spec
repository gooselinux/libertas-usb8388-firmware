Summary: Firmware for Marvell Libertas USB 8388 Network Adapter
Name:    libertas-usb8388-firmware
Version: 5.110.22.p23
Release: 3.1%{?dist}
# up the Epoch because the Marvel version scheme is less than Cozybit's
Epoch:   2
License: Redistributable, no modification permitted
Group:   System Environment/Kernel
URL:     http://www.marvell.com/
Source0: http://dev.laptop.org/pub/firmware/libertas/usb8388-%{version}.bin
Source1: http://dev.laptop.org/pub/firmware/libertas/usb8388-%{version}.bin.md5
Source2: http://dev.laptop.org/pub/firmware/libertas/LICENSE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 
BuildArch: noarch

%description
Firmware for Marvell Libertas USB 8388 Network Adapter

%prep
cp -p %{SOURCE0} .
md5sum -c %{SOURCE1}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/lib/firmware
%{__install} -m 0644 %{SOURCE0} $RPM_BUILD_ROOT/lib/firmware/usb8388.bin
%{__install} -m 0644 %{SOURCE2} $RPM_BUILD_ROOT/lib/firmware/LICENSE.usb8388
sed -i 's/\r//' $RPM_BUILD_ROOT/lib/firmware/LICENSE.usb8388

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/lib/firmware/usb8388.bin
%doc /lib/firmware/LICENSE.usb8388


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2:5.110.22.p23-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:5.110.22.p23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:5.110.22.p23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 6  2009 Peter Robinson <pbrobinson@gmail.com> - 2:5.110.22.p23-1
- update to 5.110.22.p23

* Thu Nov 20 2008 Peter Robinson <pbrobinson@gmail.com> - 2:5.110.22.p18-1
- update to 5.110.22.p18

* Tue May 27 2008 Dennis Gilmore <dennis@laptop.org> - 2:5.110.22.p14-1
- update to 5.110.22.p14
- http://dev.laptop.org/ticket/6993

* Sat Apr 12 2008 Dennis Gilmore <dennis@laptop.org> - 2:5.110.22.p6-1
- update to 5.110.22.p6
- http://dev.laptop.org/ticket/6706

* Wed Jan 30 2008 Dennis Gilmore <dennis@laptop.org> - 2:5.110.22.p1-1
- update to 5.110.22.p1 
- less racy 

* Mon Dec 31 2007 Dennis Gilmore <dennis@laptop.org> - 2:5.110.20.p49-1
- update to 5.110.20.p49 which fixes http://dev.laptop.org/ticket/5194

* Wed Dec 12 2007 Dennis Gilmore <dennis@laptop.org> - 2:5.110.20.p47-2
- fix typo in install

* Tue Dec 11 2007 Dennis Gilmore <dennis@laptop.org> - 2:5.110.20.p47-1
- update to 5.110.20.p47

* Wed Nov 21 2007 Dennis Gilmore <dennis@laptop.org> - 2:5.110.20.p4-1
- update to 5.110.20.p4

* Mon Nov 19 2007 Dennis Gilmore <dennis@laptop.org> - 2:5.110.20.p2-1
- update to 5.110.20.p2
- be consistent with paths

* Tue Nov  6 2007 C. Scott Ananian <cscott@laptop.org> - 2:5.110.20.p0-1
- Fix bugs with mesh channels 6 and 11.

* Tue Nov  6 2007 C. Scott Ananian <cscott@laptop.org> - 2:5.110.19.p6-1
- Address problems with long-lived TCP connections.
- This release known to have issues with mesh channels 6 and 11.

* Fri Oct 26 2007 John (J5) Palmieri <johnp@redhat.com> - 2:5.110.19.p0-1
- Mesh route discovery optimization resulting improved route acquisition time
- Mesh beacon control for beacon enable/disable or set beacon interval
- Wirless LEDs behavior control from the driver as per OLPC ticket 1385
- Mesh always on
- Mesh start/stop feature is added
- Dynamic RSSI fix. Bug #19730
- During scan and continous mesh data transfer a race condition detected Bug #20510

* Wed Aug 29 2007 John (J5) Palmieri <johnp@redhat.com> - 2:5.110.17.p1-0.1.20070829
- Update to an interum 5.110.17.p2 with suspend fix firmware

* Tue Aug 07 2007 John (J5) Palmieri <johnp@redhat.com> - 2:5.110.17.p0-1
- Upgrade to 5.110.17.p0
- SLEEP_ACTIVATE host command now sends a reply.
- Per packet mesh TTL. Needed driver patch:
  http://lists.infradead.org/pipermail/libertas-dev/2007-July/000580.html.
- New SET_BOOT2_VER commands (for OLPC ticket #1694). Needed driver patch:
  http://lists.infradead.org/pipermail/libertas-dev/2007-July/000547.html
- Do not detach on suspend/resume
- Support for monitor mode. Needed driver patch:
  http://lists.infradead.org/pipermail/libertas-dev/2007-July/000582.html
  plus wireshark patches available here:
  https://cozybit1.dnsalias.org/~javier/patches/wireshark-0.99.5-fw-5.220.11-support.patch
- Default TTL (=10) in RREQ frames.
- Link Loss Event is not generated when Privacy bit changes in the beacon.
- Fix MESH_AUTOSTART message flood (Trac #1936)
- Enable NULL data packet (with PM=1) with scan (Trac # 1974). NULL Data
  packet will be sent to the access point if a channel other than the
  associated channel is scanned.


* Thu Jul 12 2007 John (J5) Palmieri <johnp@redhat.com> - 2:5.110.16.p1-1
- Upgrade to 5.110.16.p1

* Mon Jul 02 2007 John (J5) Palmieri <johnp@redhat.com> - 2:5.110.16.p0-1
- Upgrade to 5.110.16.p0 on Marvell's branch
- We are now using firmware from Marvell which has a version scheme which
  starts at 5.110 so we need to update the Epoch

* Fri Jun 08 2007 John (J5) Palmieri <johnp@redhat.com> - 1:5.220.11.p5-1
- clean up spec
- Upgrade to 5.220.11.p5

* Thu Mar 30 2007 Dan Williams <dcbw@redhat.com>
- Upgrade to 5.220.10.p5

* Thu Mar 29 2007 Dan Williams <dcbw@redhat.com>
- Upgrade to 5.220.10.p4

* Tue Mar 27 2007 Marcelo Tosatti <mtosatti@redhat.com>
- Upgrade to 5.220.10.p3

* Wed Mar  21 2007 Marcelo Tosatti <mtosatti@redhat.com>
- Upgrade to 5.220.10.p0

* Tue Mar  6 2007 Marcelo Tosatti <mtosatti@redhat.com>
- Upgrade to 5.220.9.p10

* Sat Feb 17 2007 Marcelo Tosatti <mtosatti@redhat.com>
- Upgrade to 5.110.12.p0

* Tue Feb 13 2007 Marcelo Tosatti <mtosatti@redhat.com>
- Upgrade to 5.110.11.p1

* Fri Dec 29 2006 Marcelo Tosatti <mtosatti@redhat.com>
- Upgrade to 5.220.9.p5 
- Added RELEASE_NOTES file to /lib/firmware/

* Mon Dec  4 2006 Marcelo Tosatti <mtosatti@redhat.com>
- Upgrade to 5.220.9 firmware

* Tue Nov  7 2006 Christopher Blizzard <blizzard@redhat.com> - usb8388-firmware
- Initial build.

