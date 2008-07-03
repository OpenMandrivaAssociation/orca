%define pyorbit_version 2.0.1
%define pygtk2_version 2.6.2
%define gnome_python_version 2.6.2
%define brltty_version 3.7.2
%define gail_version 1.8.11
%define gnome_speech_version 0.3.10
%define eel_version 2.14.0
%define libspi_version 1.7.6

Summary: GNOME screen reader for people with visual impairments
Name: orca
Version: 2.23.4
Release: %mkrel 2
License: LGPLv2+
Group: Accessibility
URL: http://live.gnome.org/Orca/
Source0: http://ftp.gnome.org/pub/GNOME/sources/orca/orca-%{version}.tar.bz2

BuildRoot: %{_tmppath}/orca-%{version}-%{release}-buildroot
BuildRequires:  pygtk2.0-devel >= %{pygtk2_version}
BuildRequires:  pyorbit-devel >= %{pyorbit_version}
BuildRequires:	gail-devel >= %{gail_version}
BuildRequires:	eel-devel >= %{eel_version}
BuildRequires:	libat-spi-devel >= %{libspi_version}
BuildRequires:	gnome-speech-devel >= %{gnome_speech_version}
BuildRequires:  brlapi-devel
BuildRequires:	brlapi-python
BuildRequires:	gnome-python-bonobo
BuildRequires:	desktop-file-utils
BuildRequires:	chrpath
Requires: gnome-python-bonobo
Requires: pygtk2.0-libglade
Requires: python-at-spi
Requires: gnome-terminal

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

%find_lang %{name}

chrpath -d %buildroot%{py_platsitedir}/*orca*/*.so

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

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


