Summary:	xpr applications - printing X window
Summary(pl.UTF-8):   Aplikacje xpr - drukowanie okienek X
Name:		xorg-app-xpr
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Application
Source0:	http://xorg.freedesktop.org/releases/individual/app/xpr-%{version}.tar.bz2
# Source0-md5:	6b3a6896081f628bf5a2c9129417c86f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
# just xmuu
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xpr takes as input a window dump file produced by xwd and formats it
for output on PostScript printers, the Digital LN03 or LA100, the IBM
PP3812 page printer, the HP LaserJet (or other PCL printers), or the
HP PaintJet.

xdpr uses the commands xwd, xpr, and lpr or lp to dump an X window,
process it for a particular printer type, and print it out on the
printer of your choice.

%description -l pl.UTF-8
xpr przyjmuje na wejściu plik zrzutu okna utworzony przez xwd i
formatuje go do wydruku na drukarkach postscriptowych, Digital LN03
lub LA100, drukarce stronnicowej IBM PP3812, HP LaserJet (albo innych
drukarkach PCL) lub HP PaintJet.

xdpr używa poleceń xwd, xpr i lpr lub lp do wykonania zrzutu okienka
X, przetworzenia go dla danego typu drukarki i wydrukowania go na
wybranej drukarce.

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
