Summary:	Library to embed Gecko for the Mono Winforms WebControl
Summary(pl.UTF-8):	Biblioteka osadzająca Gecko dla klasy Mono Winforms WebControl
Name:		gluezilla
Version:	2.6
Release:	1
License:	LGPL v2
Group:		Libraries
# latest downloads summary at http://ftp.novell.com/pub/mono/sources-stable/
Source0:	http://ftp.novell.com/pub/mono/sources/gluezilla/%{name}-%{version}.tar.bz2
# Source0-md5:	bd4eb89747498945227877295fcd36b5
Patch0:		%{name}-xul.patch
Patch1:		%{name}-opt.patch
URL:		http://www.mono-project.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	mono-devel
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
BuildRequires:	pkgconfig
BuildRequires:	xulrunner-devel >= 1.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple library to embed Gecko (xulrunner) for the Mono Winforms
WebControl.

This is part of the Mono project.

%description -l pl.UTF-8
Prosta biblioteka osadzająca Gecko (xulrunnera) dla klasy Mono
Winforms WebControl.

Część projektu Mono.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgluezilla.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README TODO
%attr(755,root,root) %{_libdir}/libgluezilla.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgluezilla.so.0
# should be -avoid-version?
%attr(755,root,root) %{_libdir}/libgluezilla.so
