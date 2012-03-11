Summary: GNOME screen reader for people with visual impairments
Name: orca
Version: 3.2.2
Release: 1
License: LGPLv2+
Group: Accessibility
URL: http://live.gnome.org/Orca/
Source0: http://ftp.gnome.org/pub/GNOME/sources/orca/orca-%{version}.tar.xz
#BuildArch: noarch

BuildRequires:	gnome-common
Buildrequires:	gnome-doc-utils
BuildRequires:	intltool
Buildrequires:	pkgconfig(atspi-2)
Buildrequires:	pkgconfig(gtk+-3.0)
Buildrequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	python-dbus
BuildRequires:	python-cairo
BuildRequires:	pyxdg
BuildRequires:	python-speechd
BuildRequires:	python-braille
BuildRequires:	brlapi-python
BuildRequires:	python-gi
Requires:	python-dbus
Requires:	python-cairo
Requires:	pyxdg
Requires:	python-speechd
Requires:	python-braille
Requires:	brlapi-python
Requires:	pyatspi

%description
A flexible, scriptable, extensible screen reader for the GNOME platform
that provides access via speech synthesis, braille, and magnification.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README NEWS
%{_bindir}/orca
%{py_platsitedir}/*orca*
%_mandir/man1/orca.1*
%{_datadir}/orca
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_sysconfdir}/xdg/autostart/*.desktop

