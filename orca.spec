# debug is empty anyway and rpmlint rejects build
%define _enable_debug_packages %{nil}
%define debug_package %{nil}
%define _disable_rebuild_configure 1
# Bogus typelib dependencies, lets try disable it
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^typelib\\(Spiel

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	GNOME screen reader for people with visual impairments
Name:		orca
Version:	51.1
Release:	1
License:	LGPLv2+
Group:		Accessibility
Url:		https://live.gnome.org/Orca/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/orca/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	python-brlapi
BuildRequires:	python-cairo
BuildRequires:	python-gi
BuildRequires:	python%{pyver}dist(louis)
BuildRequires:	python%{pyver}dist(pyxdg)
BuildRequires:	python-speechd
BuildRequires:  brlapi-devel
BuildRequires:	pkgconfig(atspi-2)
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  at-spi2-core
BuildRequires:	pkgconfig(gnome-doc-utils) >= 0.17.3
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.1.14
BuildRequires:	pkgconfig(liblouis)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.90.3
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(python3)
BuildRequires:  python-dasbus
BuildRequires:  python-psutil
Requires:	python-atspi
Requires:	python-brlapi
Requires:	python-cairo
Requires:	python%{pyver}dist(louis)
Requires:	python%{pyver}dist(pyxdg)
Requires:	python-speechd
Requires: python-dasbus
Requires: python-psutil
Requires: speech-dispatcher
Requires: libwnck3
Requires: typelib(Wnck)
Requires: gsettings-desktop-schemas
Requires: dconf
Requires: python-gi
Requires: python-gobject3
Requires: gtk+3.0
Requires: gstreamer1.0-plugins-good
Requires: gstreamer1.0-plugins-base
Recommends: espeak-ng

%description
A flexible, scriptable, extensible screen reader for the GNOME platform
that provides access via speech synthesis, braille, and magnification.

%prep
%autosetup -p1

%build
# MathCAT (MathML support) requires Rust. Lets disable it for now.
%meson -Dmathcat=false
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README* NEWS
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%{_bindir}/%{name}
%{py_puresitedir}/*orca*
#{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}*.*
%{_mandir}/man1/%{name}.1*
%{_prefix}/lib/systemd/user/orca.service
%{_datadir}/applications/orca.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Orca.gschema.xml
