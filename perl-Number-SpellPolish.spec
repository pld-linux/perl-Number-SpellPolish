#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Number
%define	pnam	SpellPolish
Summary:	Number::SpellPolish -- spell out number in Polish
Summary(pl):	Number::SpellPolish -- wymawianie liczb po polsku
Name:		perl-%{pdir}-%{pnam}
Version:	0.7
Release:	2
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://radek.karnet.pl/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module provides functionality for spelling out numbers and
prices in Polish language. If you don't speak polish, you probably
won't need it.

This module *is not* a subclass of Number::Spell.

%description -l pl
Ten modu� perla daje mo�liwo�� zapisu liczb i cen w j�zyku polskim.
Nie znaj�cym polskiego ten modu� jest raczej zb�dny.

Ten modu� nie jest podklas� Number::Spell.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Number/SpellPolish.pm
%{_mandir}/man3/*