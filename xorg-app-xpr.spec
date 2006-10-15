Summary:	xpr application
Summary(pl):	Aplikacja xpr
Name:		xorg-app-xpr
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Application
Source0:	http://xorg.freedesktop.org/releases/individual/app/xpr-%{version}.tar.bz2
# Source0-md5:	01c0a14755fc91369e8c011c9f881d5d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
# just xmuu
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xpr application.

%description -l pl
Aplikacja xpr.

%prep
%setup -q -n xpr-%{version}

%build
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xdpr
%attr(755,root,root) %{_bindir}/xpr
%{_mandir}/man1/xdpr.1x*
%{_mandir}/man1/xpr.1x*
