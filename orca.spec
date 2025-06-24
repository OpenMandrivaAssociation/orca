# debug is empty anyway and rpmlint rejects build
%define _enable_debug_packages %{nil}
%define debug_package %{nil}
%define _disable_rebuild_configure 1
# Bogus typelib dependencies, lets try disable it
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^typelib\\(Spiel

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	GNOME screen reader for people with visual impairments
Name:		orca
Version:	48.5
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
BuildRequires:	python3-louis
BuildRequires:	python-xdg
BuildRequires:	python-speechd
BuildRequires:	pkgconfig(atspi-2)
BuildRequires:	pkgconfig(gnome-doc-utils) >= 0.17.3
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.1.14
BuildRequires:	pkgconfig(liblouis)
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.90.3
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(python)
Requires:	python-atspi
Requires:	python-brlapi
Requires:	python-cairo
Requires:	python3-louis
Requires:	python-xdg
Requires:	python-speechd

%description
A flexible, scriptable, extensible screen reader for the GNOME platform
that provides access via speech synthesis, braille, and magnification.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README* NEWS
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%{_bindir}/%{name}
%{py_puresitedir}/*orca*
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}*.*
%{_mandir}/man1/%{name}.1*
