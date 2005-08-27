# $Rev: 3412 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	xpr application
Summary(pl):	Aplikacja xpr
Name:		xorg-app-xpr
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Application
######		Unknown group!
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xpr-%{version}.tar.bz2
# Source0-md5:	be1e2a72a0c78b2d282fd63fb60ec509
Patch0:		xpr-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/xpr-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xpr application.

%description -l pl
Aplikacja xpr.


%prep
%setup -q -n xpr-%{version}
%patch0 -p1


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
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
