%define name murrine-themes
%define version 2.0
%define release 7

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
Source11: Murreza.tar.lzma
Source12: Murrine-Sky.tar.lzma
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
%__lzma -dc %SOURCE11 | %__tar fx - -C %{buildroot}%{themesdir}
%__lzma -dc %SOURCE12 | %__tar fx - -C %{buildroot}%{themesdir}

%__mv %{buildroot}%{themesdir}/Murreza/* %{buildroot}%{themesdir}/
%__rm -rf %{buildroot}%{themesdir}/Murreza

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{themesdir}/*



%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0-6mdv2011.0
+ Revision: 612969
- the mass rebuild of 2010.1 packages

* Tue May 04 2010 Lev Givon <lev@mandriva.org> 2.0-5mdv2010.1
+ Revision: 542132
- Update.

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.0-4mdv2010.0
+ Revision: 430136
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 2.0-3mdv2009.0
+ Revision: 253370
- rebuild

* Mon Mar 10 2008 Lev Givon <lev@mandriva.org> 2.0-1mdv2008.1
+ Revision: 183802
- Add new themes.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Lev Givon <lev@mandriva.org> 1.0-1mdv2008.1
+ Revision: 103287
- import murrine-themes


* Mon Oct 29 2007 Lev Givon <lev@mandriva.org> 1.0-1mdv2008.0 
- Package for Mandriva.
