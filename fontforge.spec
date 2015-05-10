Summary:	An outline font editor
Summary(pl.UTF-8):	Edytor fontów rysowanych
Name:		fontforge
Version:	20120731
Release:	5
License:	BSD
Group:		X11/Applications/Publishing
Source0:	http://downloads.sourceforge.net/fontforge/%{name}_full-%{version}-b.tar.bz2
# Source0-md5:	a8a90473a97da87e45f66d11007b6e7c
Patch0:		%{name}-link.patch
Patch1:		%{name}-20090224-pythondl.patch
Patch2:		giflib5.patch
URL:		http://fontforge.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.2
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gettext-tools
BuildRequires:	giflib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libspiro-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libuninameslist-devel
BuildRequires:	libxml2-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.3
BuildRequires:	python-modules >= 2.3
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	zlib-devel
Requires:	cairo >= 1.2
Requires:	iconv
Obsoletes:	pfaedit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FontForge allows you to edit outline and bitmap fonts. You can create
new ones or modify old ones. It is also a font format converter and
can convert among PostScript (ASCII & binary Type 1, some Type 3s,
some Type 0s), TrueType, OpenType (Type2) and CID-keyed fonts.

FontForge used to be called PfaEdit.

%description -l pl.UTF-8
FontForge pozwala na edycję fontów rysowanych i bitmapowych. Można
tworzyć nowe lub modyfikować istniejące. Jest to także konwerter
między formatami fontów - potrafi obsługiwać fonty postscriptowe
(ASCII i binarne Type 1, część Type 3, część Type 0), TrueType,
OpenType (Type2) i fonty z kluczami CID.

FontForge wcześniej nazywał się PfaEdit.

%package devel
Summary:	Header files for FontForge libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek FontForge
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.2
Requires:	fontconfig-devel
Requires:	freetype-devel >= 2.0.0
Requires:	giflib-devel
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libspiro-devel
Requires:	libtiff-devel
Requires:	libuninameslist-devel
Requires:	libxml2-devel
Requires:	pango-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXi-devel
Requires:	zlib-devel

%description devel
Header files for FontForge libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek FontForge.

%prep
%setup -q -n %{name}-%{version}-b
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-type3 \
	--enable-multilayer \
	--enable-devicetables \
	--enable-longdouble \
	--enable-gb12345 \
	--enable-pasteafter \
	--enable-tilepath \
	--enable-pyextension \
	--with-freetype-bytecode \
	--with-regular-link \
	--without-freetype-src \
	--with-pango \
	--with-cairo \
	--with-x

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang FontForge

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f FontForge.lang
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README-Unix.html
%attr(755,root,root) %{_bindir}/fontforge
%attr(755,root,root) %{_bindir}/fontimage
%attr(755,root,root) %{_bindir}/fontlint
%attr(755,root,root) %{_bindir}/sfddiff
%attr(755,root,root) %{_libdir}/libfontforge.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfontforge.so.1
%attr(755,root,root) %{_libdir}/libgdraw.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdraw.so.4
%attr(755,root,root) %{_libdir}/libgioftp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgioftp.so.1
%attr(755,root,root) %{_libdir}/libgunicode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgunicode.so.3
%attr(755,root,root) %{_libdir}/libgutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgutils.so.1
%{_datadir}/fontforge
%{_mandir}/man1/fontforge.1*
%{_mandir}/man1/fontimage.1*
%{_mandir}/man1/fontlint.1*
%{_mandir}/man1/sfddiff.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfontforge.so
%attr(755,root,root) %{_libdir}/libgdraw.so
%attr(755,root,root) %{_libdir}/libgioftp.so
%attr(755,root,root) %{_libdir}/libgunicode.so
%attr(755,root,root) %{_libdir}/libgutils.so
%{_libdir}/libfontforge.la
%{_libdir}/libgdraw.la
%{_libdir}/libgioftp.la
%{_libdir}/libgunicode.la
%{_libdir}/libgutils.la
%{_includedir}/fontforge
%{_pkgconfigdir}/fontforge.pc
