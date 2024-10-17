%define name    xsmbrowser 
%define version 3.4.0
%define release 11

Summary: Tcl/Tk based Samba shares browser
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Source1: %{name}-commands.bz2
URL: https://www.public.iastate.edu/~chadspen/
License: GPL
Group: Networking/File transfer
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Requires: expect

%description
xSMBrowser is a fully-capable Samba browsing utility which supports both
WINS and Broadcast networks. It's been tested to work on Redhat, SuSe, DEC
Alphas, and others. It browses all aspects of networks: workgroups,
computers, shares, and files. The ability to add more than one network is
included, and the interface resembles Netscape Navigator (back/forward
buttons, stop, favorites). Mount/unmount buttons are also included.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -n %{name}-%{version}

%build
# no build for noarch packages
perl -pi -e "s|set image_path \"pixmaps\"|set image_path \"%_datadir/pixmaps/xsmbrowser\"||g;" xsmbrowser

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_bindir},/etc,%_datadir/pixmaps/xsmbrowser}/
install -m 755 xsmbrowser  \
  $RPM_BUILD_ROOT%{_bindir}
install -m 644  pixmaps/*   \
  $RPM_BUILD_ROOT%_datadir/pixmaps/xsmbrowser/

# install KDE xsmbrowser-commands file
install -m 644  %{SOURCE1}  $RPM_BUILD_ROOT/etc/
bunzip2 $RPM_BUILD_ROOT/etc/*.bz2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc INSTALL
%config(noreplace) %_sysconfdir/*
%_bindir/xsmbrowser
%dir %_datadir/pixmaps/xsmbrowser/
%_datadir/pixmaps/xsmbrowser/*



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 3.4.0-10mdv2010.0
+ Revision: 435297
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.4.0-9mdv2009.0
+ Revision: 262707
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.4.0-8mdv2009.0
+ Revision: 257752
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 3.4.0-6mdv2008.1
+ Revision: 130554
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import xsmbrowser


* Tue Apr 26 2005 Lenny Cartier <lenny@mandrakesoft.com> 3.4.0-6mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.4.0-5mdk
- rebuild

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.4.0-4mdk
- rebuild

* Tue May 07 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.4.0-3mdk
- remove useless prefix
- add missing requires on expect

* Fri Aug 24 2001 Etienne Faure <etienne@mandrakesoft.com> 3.4.0-2mdk
- rebuild

* Tue Mar 06 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.4.0-1mdk
- updated to 3.4.0

* Thu Dec 28 2000 Lenny Cartier <lenny@mandrakesoft.com> 3.3.0-1mdk
- used srpm from rufus t firefly <rufus.t.firefly@linux-mandrake.com> :
	- v3.3.0-1mdk

* Mon Dec 04 2000 rufus t firefly <rufus.t.firefly@linux-mandrake.com>
  - v3.2-1mdk
  - added xsmbrowser-commands for KDE desktop

* Tue Nov 21 2000 rufus t firefly <rufus.t.firefly@linux-mandrake.com>
  - v3.0-1mdk
  - added perl patch for the pixmaps directory

* Wed May 31 2000 rufus t firefly <rufus.t.firefly@linux-mandrake.com>
  - v2.4.0 (initial packaging)
  - bz2 archive for Mandrake

