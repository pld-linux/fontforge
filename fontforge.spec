Summary:	An outline font editor
Summary(pl):	Edytor fontów rysowanych
Name:		fontforge
Version:	20040418
Release:	1
License:	BSD
Group:		X11/Applications/Publishing
Source0:	http://fontforge.sourceforge.net/%{name}_full-%{version}.tgz
# Source0-md5:	6ff18b8ec8705a6635772f2a70524338
Patch0:		%{name}-sonames.patch
Patch1:		%{name}-iconv-in-libc.patch
URL:		http://fontforge.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
# needed at build time to not disable their support and for detecting SONAME
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libungif-devel
BuildRequires:	libuninameslist-devel
Obsoletes:	pfaedit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FontForge allows you to edit outline and bitmap fonts. You can create
new ones or modify old ones. It is also a font format converter and
can convert among PostScript (ASCII & binary Type 1, some Type 3s,
some Type 0s), TrueType, OpenType (Type2) and CID-keyed fonts.

FontForge used to be called PfaEdit.

%description -l pl
FontForge pozwala na edycjê fontów rysowanych i bitmapowych. Mo¿na
tworzyæ nowe lub modyfikowaæ istniej±ce. Jest to tak¿e konwerter
miêdzy formatami fontów - potrafi obs³ugiwaæ fonty postscriptowe
(ASCII i binarne Type 1, czê¶æ Type 3, czê¶æ Type 0), TrueType,
OpenType (Type2) i fonty z kluczami CID.

FontForge wcze¶niej nazywa³ siê PfaEdit.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-freetype-bytecode \
	--without-freetype-src

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README
%attr(755,root,root) %{_bindir}/fontforge
%attr(755,root,root) %{_bindir}/sfddiff
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_datadir}/fontforge
%lang(de) %{_datadir}/fontforge/pfaedit-de.ui
%{_datadir}/fontforge/pfaedit-en.ui
%lang(es) %{_datadir}/fontforge/pfaedit-es.ui
%lang(fr) %{_datadir}/fontforge/pfaedit-fr.ui
%lang(it) %{_datadir}/fontforge/pfaedit-it.ui
%lang(ja) %{_datadir}/fontforge/pfaedit-ja.ui
%lang(ru) %{_datadir}/fontforge/pfaedit-ru.ui
%{_mandir}/man1/*
