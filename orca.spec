%define pyorbit_version 2.0.1
%define pygtk2_version 2.6.2
%define gnome_python_version 2.6.2
%define brltty_version 3.7.2
%define gail_version 1.8.11
%define gnome_speech_version 0.3.10

Summary: GNOME screen reader for people with visual impairments
Name: orca
Version: 3.0.0
Release: %mkrel 1
License: LGPLv2+
Group: Accessibility
URL: http://live.gnome.org/Orca/
Source0: http://ftp.gnome.org/pub/GNOME/sources/orca/orca-%{version}.tar.bz2

BuildRoot: %{_tmppath}/orca-%{version}-%{release}-buildroot
BuildRequires:  pygtk2.0-devel >= %{pygtk2_version}
BuildRequires:  pyorbit-devel >= %{pyorbit_version}
BuildRequires:	gail-devel >= %{gail_version}
BuildRequires:	gnome-speech-devel >= %{gnome_speech_version}
BuildRequires:	python-at-spi
BuildRequires:  brlapi-devel
BuildRequires:	brlapi-python
BuildRequires:	gnome-python-bonobo
BuildRequires:	python-dbus
BuildRequires:	pyxdg
#gw for wnck:
BuildRequires:	gnome-python-desktop
BuildRequires:	gnome-python-gconf
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildArch: noarch
Requires: gnome-python-bonobo
Requires: gnome-python-desktop
Requires: gnome-python-gconf
Requires: python-dbus
Requires: pyxdg
Requires: pygtk2.0
Requires: python-at-spi
Requires: python-at-spi
Requires: gnome-terminal
Requires: brlapi-python

%description
A flexible, scriptable, extensible screen reader for the GNOME platform
that provides access via speech synthesis, braille, and magnification.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-MoreApplications-Accessibility" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README NEWS
%{_bindir}/orca
%{py_platsitedir}/*orca*
%_mandir/man1/orca.1*
%{_datadir}/orca
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_sysconfdir}/xdg/autostart/*.desktop
