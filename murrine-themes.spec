%define name murrine-themes
%define version 2.0
%define release %mkrel 1

%define themesdir %{_datadir}/themes

Summary: Themes for Murrine
Name:    %{name}
Version: %{version}
Release: %{release}
Source0: MurrinaAquaIsh.tar.lzma
Source1: MurrinaBlue.tar.lzma
Source2: MurrinaElement.tar.lzma
Source3: MurrinaFancyCandy.tar.lzma
Source4: MurrinaGilouche.tar.lzma
Source5: MurrinaLoveGray.tar.lzma
Source6: MurrinaOransun.tar.lzma
Source7: MurrinaTango.tar.lzma
Source8: MurrinaVerdeOlivo.tar.lzma
Source9: MurrineRounded.tar.lzma
Source10: MurrineThemePack.tar.lzma
License: GPL
Group: Graphical desktop/GNOME
Url:   http://www.cimitan.com/murrine/themes/gallery
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: murrine

%description
Various GTK2 and Metacity themes for the Murrine GTK2.x engine.

%prep

%build

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{themesdir}
%__lzma -dc %SOURCE0 | %__tar fx - -C %{buildroot}%{themesdir}
%__lzma -dc %SOURCE1 | %__tar fx - -C %{buildroot}%{themesdir}
%__lzma -dc %SOURCE2 | %__tar fx - -C %{buildroot}%{themesdir}
%__lzma -dc %SOURCE3 | %__tar fx - -C %{buildroot}%{themesdir}
%__lzma -dc %SOURCE4 | %__tar fx - -C %{buildroot}%{themesdir}
%__lzma -dc %SOURCE5 | %__tar fx - -C %{buildroot}%{themesdir}
%__lzma -dc %SOURCE6 | %__tar fx - -C %{buildroot}%{themesdir}
%__lzma -dc %SOURCE7 | %__tar fx - -C %{buildroot}%{themesdir}
%__lzma -dc %SOURCE8 | %__tar fx - -C %{buildroot}%{themesdir}
%__lzma -dc %SOURCE9 | %__tar fx - -C %{buildroot}%{themesdir}
%__lzma -dc %SOURCE10 | %__tar fx - -C %{buildroot}%{themesdir}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{themesdir}/*

