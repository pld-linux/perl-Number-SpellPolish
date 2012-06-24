
%include	/usr/lib/rpm/macros.perl
%define	pdir	Number
%define	pnam	SpellPolish

Summary:      Number-SpellPolish perl module
Summary(pl):	Modu� perla Number-SpellPolish
Name:         perl-%{pdir}-%{pnam}
Version:      0.5
Release:      1
License:      LGPL
Group:        Development/Languages/Perl
Source0:      http://radek.karnet.pl/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires: rpm-perlprov >= 3.0.3-16
BuildRequires: perl >= 5.6
BuildArch: noarch
BuildRoot: %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module provides functionality for spelling out numbers and 
prices in Polish language. If you don't speak polish, you probably won't
need it.

This module *is not* a subclass of Number::Spell.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

gzip -9nf Changes README LICENSE

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
