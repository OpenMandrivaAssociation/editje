#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/editje editje; \
#cd editje; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#VERSION=$(cat configure.ac | grep "editje" | grep INIT | sed 's@\[@@g' | sed 's@\]@@g' | sed 's@)@@g' | cut -d, -f 2 | sed "s@ @@"); \
#PKG_VERSION=$VERSION.$SVNREV; \
#cd ..; \
#tar -Jcf editje-$PKG_VERSION.tar.xz editje/ --exclude .svn --exclude .*ignore

%define svndate	20110824
%define svnrev	66406

Summary:	Edje editor oriented towards UI design
Name:		editje
Version:	0.9.3
Release:	0.%{svnrev}.1
License:	LGPL,GPLv3
Group:		Graphical desktop/Enlightenment
URL:		http://enlightenment.org/
Source0: 	%{name}-%{version}.%{svnrev}.tar.xz

BuildRequires:	edje
BuildRequires:	embryo
BuildRequires: 	gettext-devel
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
%setup -qn %{name}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x 
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%doc AUTHORS COPYING README
%{_bindir}/*
%{_bindir}/editje-bin
%{_datadir}/applications/editje.desktop
%{_datadir}/application-registry/editje.applications
%{_iconsdir}/editje.png
%{_datadir}/%{name}
%{py_puresitedir}/%{name}/*

