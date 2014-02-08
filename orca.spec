# debug is empty anyway and rpmlint rejects build

%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	GNOME screen reader for people with visual impairments
Name:		orca
Version:	3.6.2
Release:	2
License:	LGPLv2+
Group:		Accessibility
URL:		http://live.gnome.org/Orca/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	brlapi-python
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	python-gi
BuildRequires:	pkgconfig(atspi-2)
BuildRequires:	pkgconfig(gnome-doc-utils) >= 0.17.3
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.1.14
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.90.3
BuildRequires:	pkgconfig(python)
BuildRequires:	python-dbus
BuildRequires:	python-cairo
BuildRequires:	python-pyxdg
BuildRequires:	python-speechd
BuildRequires:	python-braille
BuildRequires:	itstool
Requires:	python-dbus
Requires:	python-cairo
Requires:	python-pyxdg
Requires:	python-speechd
Requires:	python-braille
Requires:	brlapi-python
Requires:	python-pyatspi

%description
A flexible, scriptable, extensible screen reader for the GNOME platform
that provides access via speech synthesis, braille, and magnification.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README NEWS
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%{_bindir}/%{name}
%{py_platsitedir}/*orca*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*
