# FIXME: xulrunner-devel is missing sdk (libs, collected headers)
Summary:	Library to embed Gecko for the Mono Winforms WebControl
Summary(pl.UTF-8):	Biblioteka osadzająca Gecko dla klasy Mono Winforms WebControl
Name:		gluezilla
Version:	1.9.1
Release:	0.1
License:	LGPL v2
Group:		Libraries
# latest downloads summary at http://ftp.novell.com/pub/mono/sources-stable/
Source0:	http://ftp.novell.com/pub/mono/sources/gluezilla/%{name}-%{version}.tar.bz2
# Source0-md5:	c9d143cd531ff978da8e6b417e0d65d2
URL:		http://www.mono-project.com/
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	libstdc++-devel
BuildRequires:	mono-devel
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
BuildRequires:	pkgconfig
BuildRequires:	xulrunner-devel >= 1.8
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

%build
%configure

# FIXME:
# all needed headers are present (symlinked?) in sdk/include dir (missing in xulrunner-devel)
# libxpcomglue is missing in xulrunner-devel (present in sdk/lib subdir of xulrunner dist dir)
base=$(pkg-config --variable=includedir xulrunner-xpcom)
flags="%{rpmcxxflags}"
for d in dom embed_base necko pipboot pipnss pref shistory uriloader webbrwsr windowwatcher ; do
	flags="$flags -I$base/$d"
done
%{__make} \
	AM_CXXFLAGS="$flags" \
	AM_LDFLAGS="-L../../xulrunner-1.8.1.14/mozilla/dist/sdk/lib"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libgluezilla.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
# LICENSE missing in tarball
%attr(755,root,root) %{_libdir}/libgluezilla.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgluezilla.so.0
# should be -avoid-version?
%attr(755,root,root) %{_libdir}/libgluezilla.so
