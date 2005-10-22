Summary:	xpr application
Summary(pl):	Aplikacja xpr
Name:		xorg-app-xpr
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Application
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/app/xpr-%{version}.tar.bz2
# Source0-md5:	71101cc19dd6f8bf6b437b5b4935d83f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
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
	DESTDIR=$RPM_BUILD_ROOT \
	appmandir=%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1x*
