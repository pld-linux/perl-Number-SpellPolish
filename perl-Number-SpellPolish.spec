%include	/usr/lib/rpm/macros.perl

%define		pdir	Number
%define		pnam	SpellPolish

Summary:	Number-SpellPolish perl module
Summary(pl):	Modu³ perla Number-SpellPolish
Name:		perl-%{pdir}-%{pnam}
Version:	0.5
Release:	3
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://radek.karnet.pl/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-Autoloader.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module provides functionality for spelling out numbers and
prices in Polish language. If you don't speak polish, you probably
won't need it.

This module *is not* a subclass of Number::Spell.

%description -l pl
Ten modu³ perla daje mo¿liwo¶æ zapisu liczb i cen w jêzyku polskim.
Nie znaj±cym polskiego ten modu³ jest raczej zbêdny.

Ten modu³ nie jest podklas± Number::Spell.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make}

gzip -9nf Changes README

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Number/SpellPolish.pm
%{_mandir}/man3/*
