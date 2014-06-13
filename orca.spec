# debug is empty anyway and rpmlint rejects build
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	GNOME screen reader for people with visual impairments
Name:		orca
Version:	3.8.2
Release:	6
License:	LGPLv2+
Group:		Accessibility
Url:		http://live.gnome.org/Orca/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/orca/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	python3-brlapi
BuildRequires:	python3-cairo
BuildRequires:	python3-gi
BuildRequires:	python3-louis
BuildRequires:	python3-xdg
BuildRequires:	python3-speechd
BuildRequires:	pkgconfig(atspi-2)
BuildRequires:	pkgconfig(gnome-doc-utils) >= 0.17.3
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.1.14
BuildRequires:	pkgconfig(liblouis)
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.90.3
BuildRequires:	pkgconfig(python3)
Requires:	python3-atspi
Requires:	python3-brlapi
Requires:	python3-cairo
Requires:	python3-louis
Requires:	python3-xdg
Requires:	python3-speechd

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
%{py3_platsitedir}/*orca*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*

