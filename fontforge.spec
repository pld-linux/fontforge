#
# Conditional build:
%bcond_with	python		# Python scripting
%bcond_without	static_libs	# static libraries

Summary:	An outline font editor
Summary(pl.UTF-8):	Edytor fontów rysowanych
Name:		fontforge
Version:	20170731
Release:	1
License:	GPL v3+ with BSD parts
Group:		X11/Applications/Publishing
#Source0Download: https://github.com/fontforge/fontforge/releases
Source0:	https://github.com/fontforge/fontforge/releases/download/%{version}/%{name}-dist-%{version}.tar.xz
# Source0-md5:	8a717035915ab4cd78b89b0942dfa1fc
Patch0:		%{name}-link.patch
Patch1:		%{name}-libexecdir.patch
URL:		http://fontforge.github.io/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.6
BuildRequires:	czmq-devel >= 2.2.0
BuildRequires:	czmq-devel < 4
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 1:2.3.7
BuildRequires:	gettext-tools
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	gtk+2-devel >= 1:2.0
%{?with_python:BuildRequires:	python-ipython}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
# TODO: 1:0.6 when released
BuildRequires:	libspiro-devel >= 1:0.2
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libltdl-devel >= 2:2
BuildRequires:	libtool >= 2:2
# 0.3
BuildRequires:	libuninameslist-devel >= 20130501
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pango-devel >= 1:1.10
BuildRequires:	pkgconfig >= 1:0.25
BuildRequires:	python-devel >= 2.3
BuildRequires:	python-modules >= 2.3
BuildRequires:	readline-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xz
BuildRequires:	zeromq-devel >= 4.0.4
BuildRequires:	zlib-devel
Requires:	cairo >= 1.6
Requires:	czmq >= 2.2.0
Requires:	glib2 >= 1:2.6
Requires:	iconv
Requires:	libuninameslist >= 20130501
Requires:	pango >= 1:1.10
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
Requires:	cairo-devel >= 1.6
Requires:	fontconfig-devel
Requires:	freetype-devel >= 1:2.3.7
Requires:	giflib-devel
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libspiro-devel >= 1:0.2
Requires:	libtiff-devel >= 4
Requires:	libuninameslist-devel >= 20130501
Requires:	libxml2-devel >= 2.0
Requires:	pango-devel >= 1:1.10
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXi-devel
Requires:	zlib-devel

%description devel
Header files for FontForge libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek FontForge.

%package static
Summary:	Static FontForge libraries
Summary(pl.UTF-8):	Statyczne biblioteki FontForge
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FontForge libraries.

%description static -l pl.UTF-8
Statyczne biblioteki FontForge.

%package doc
Summary:	FontForge documentation
Summary(pl.UTF-8):	Dokumentacja do FontForge
Group:		Documentation

%description doc
FontForge documentation.

%description doc -l pl.UTF-8
Dokumentacja do FontForge.

%package -n python-fontforge
Summary:	Python bindings for FontForge libraries
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek FontForge
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-fontforge
Python bindings for FontForge libraries.

%description -n python-fontforge -l pl.UTF-8
Wiązania Pythona do bibliotek FontForge.

%prep
%setup -q -n %{name}-2.0.%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PO_TRACE=/usr/bin/potrace \
	UPDATE_MIME_DATABASE=/usr/bin/update-mime-database \
	UPDATE_DESKTOP_DATABASE=/usr/bin/update-desktop-database \
	--enable-debug-raw-points \
	--enable-devicetables \
	--enable-gb12345 \
	--enable-gtk2-use \
	--enable-longdouble \
	--enable-multilayer \
	--enable-pasteafter \
	--enable-pyextension \
	--enable-python-even \
	--disable-silent-rules \
	--enable-tile-path \
	--enable-type3 \
	--enable-write-pfm \
	--with-cairo \
	--with-freetype-bytecode \
	--without-freetype-src \
	--with-pango \
	--with-regular-link \
	--with-x

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/fontforge/plugins/*.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/fontforge/plugins/*.a
%endif

%find_lang FontForge

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f FontForge.lang
%defattr(644,root,root,755)
%doc AUTHORS LICENSE doc/{README-unix,README-Unix.html}
%attr(755,root,root) %{_bindir}/fontforge
%attr(755,root,root) %{_bindir}/fontimage
%attr(755,root,root) %{_bindir}/fontlint
%attr(755,root,root) %{_bindir}/sfddiff
%attr(755,root,root) %{_libdir}/libfontforge.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfontforge.so.2
%attr(755,root,root) %{_libdir}/libfontforgeexe.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfontforgeexe.so.2
%attr(755,root,root) %{_libdir}/libgdraw.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdraw.so.5
%attr(755,root,root) %{_libdir}/libgioftp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgioftp.so.2
%attr(755,root,root) %{_libdir}/libgunicode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgunicode.so.4
%attr(755,root,root) %{_libdir}/libgutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgutils.so.2
%attr(755,root,root) %{_libdir}/libzmqcollab.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzmqcollab.so.2
%dir %{_libdir}/fontforge
%dir %{_libdir}/fontforge/plugins
%attr(755,root,root) %{_libdir}/fontforge/plugins/gb12345.so
%dir %{_libexecdir}/FontForgeInternal
%attr(755,root,root) %{_libexecdir}/FontForgeInternal/fontforge-internal-collab-server
%{_datadir}/fontforge
%{_datadir}/mime/packages/fontforge.xml
%{_desktopdir}/fontforge.desktop
%{_iconsdir}/hicolor/*x*/apps/fontforge.png
%{_iconsdir}/hicolor/scalable/apps/fontforge.svg
%{_mandir}/man1/fontforge.1*
%{_mandir}/man1/fontimage.1*
%{_mandir}/man1/fontlint.1*
%{_mandir}/man1/sfddiff.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfontforge.so
%attr(755,root,root) %{_libdir}/libfontforgeexe.so
%attr(755,root,root) %{_libdir}/libgdraw.so
%attr(755,root,root) %{_libdir}/libgioftp.so
%attr(755,root,root) %{_libdir}/libgunicode.so
%attr(755,root,root) %{_libdir}/libgutils.so
%attr(755,root,root) %{_libdir}/libzmqcollab.so
%{_includedir}/fontforge
%{_pkgconfigdir}/libfontforge.pc
%{_pkgconfigdir}/libfontforgeexe.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libfontforge.a
%{_libdir}/libfontforgeexe.a
%{_libdir}/libgdraw.a
%{_libdir}/libgioftp.a
%{_libdir}/libgunicode.a
%{_libdir}/libgutils.a
%{_libdir}/libzmqcollab.a
%endif

%files doc
%defattr(644,root,root,755)
%{_docdir}/fontforge

%files -n python-fontforge
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/fontforge.so
%attr(755,root,root) %{py_sitedir}/psMat.so
