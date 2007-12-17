%define name murrine-themes
%define version 1.0
%define release %mkrel 1

%define themesdir %{_datadir}/themes

Summary: Themes for Murrine
Name:    %{name}
Version: %{version}
Release: %{release}
Source0: MurrinaAquaIsh.tar.bz2
Source1: MurrinaFancyCandy.tar.bz2
Source2: MurrinaGilouche.tar.bz2
Source3: MurrinaLoveGray.tar.bz2
Source4: MurrinaVerdeOlivo.tar.bz2
Source5: MurrineRounded.tar.bz2
Source6: MurrineThemePack.tar.bz2
License: GPL
Group: Graphical desktop/GNOME
Url: http://cimi.netsons.org/pages/murrine.php
BuildArch: noarch
Requires: murrine

%description
Various GTK2 and Metacity themes for the Murrine GTK2.x engine.

%prep

%build

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{themesdir}
%__tar jfx %SOURCE0 -C %{buildroot}%{themesdir}
%__tar jfx %SOURCE1 -C %{buildroot}%{themesdir}
%__tar jfx %SOURCE2 -C %{buildroot}%{themesdir}
%__tar jfx %SOURCE3 -C %{buildroot}%{themesdir}
%__tar jfx %SOURCE4 -C %{buildroot}%{themesdir}
%__tar jfx %SOURCE5 -C %{buildroot}%{themesdir}
%__tar jfx %SOURCE6 -C %{buildroot}%{themesdir}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{themesdir}/*

