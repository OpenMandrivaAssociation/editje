%define _enable_debug_packages %{nil}
%define debug_package %{nil}


%define gitdate 20150504
# didn't change anything since date above up to r76819
%define svnrev 76819

Summary:	Edje editor oriented towards UI design
Name:		editje
Version:	0.9.3
Release:	0.%{gitdate}.1
License:	LGPL,GPLv3
Group:		Graphical desktop/Enlightenment
URL:		http://enlightenment.org/
Source0: 	%{name}-%{version}.%{gitdate}.tar.gz

BuildRequires:	edje
BuildRequires:	embryo
BuildRequires:	evas
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(elementary)
BuildRequires:	pkgconfig(embryo)

Requires:	edje
Requires:	python-ecore
Requires:	python-evas
Requires:	python-elementary
Requires:	python-edje
Requires:	python-e_dbus

%description
Editje is an Edje editor oriented towards UI design, and not just being 
a GUI over the edc syntax. It provides three major modes: standard 
edition, animations and signals management.

%prep
%setup -qn %{name}-%{version}.%{gitdate}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README
%{_bindir}/editje-bin
%{_datadir}/applications/editje.desktop
%{_datadir}/application-registry/editje.applications
%{_iconsdir}/editje.png
%{_datadir}/%{name}
%{py_puresitedir}/%{name}/*

%changelog
* Wed Jan 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.9.3-0.66406.1
+ Revision: 759801
- added missing BR evas
- fixed group
- imported package editje


* Wed Aug 24 2011 Gianvacca <gianvacca@unity-linux.org> 0.9.3.61974-0.20110824.1-unity2011
- new snapshot

* Sat Mar 05 2011 OnlyHuman <halo.3.0sdt@googlemail.com> 0.0.1-0.20110305.1-unity2011
- new snapshot 20110305

* Fri Jan 14 2011 OnlyHuman <halo.3.0sdt@googlemail.com> 0.0.1-0.20110114.1-unity2011
- new snapshot 20110114

* Wed Dec 13 2010 OnlyHuman <halo.3.0sdt@googlemail.com> 0.0.1-0.20101203.1-unity2010
- new snapshot 20101203

* Wed Oct 13 2010 mdawkins <mattydaw@gmail.com> 0.0.1-0.20101006.1-unity2010
- new snapshot 20101006

* Wed Aug 25 2010 mdawkins <mattydaw@gmail.com> 0.0.1-0.20100825.1-unity2010
 first build
