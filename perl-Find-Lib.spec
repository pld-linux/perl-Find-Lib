#
# TODO: - fix "make test"
#	- pl
#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_with	tests		# do not perform "make test"
#
%define		pdir	Find
%define		pnam	Lib
Summary:	Find::Lib - helper to smartly find libs to use in the filesystem tree
Name:		perl-Find-Lib
Version:	1.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/Y/YA/YANNK/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bf5619b4ba1945320eccef69b028c453
URL:		http://search.cpan.org/dist/Find-Lib/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Helper to smartly find libs to use in the filesystem tree.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{_mandir}/man3/Find::Lib.3pm*
%dir %{perl_vendorlib}/Find
%{perl_vendorlib}/Find/Lib.pm
