#
# Conditional build:
%bcond_without	python		# Python (3) scripting and extension
%bcond_without	doc		# Sphinx documentation

Summary:	An outline font editor
Summary(pl.UTF-8):	Edytor fontów rysowanych
Name:		fontforge
Version:	20230101
Release:	2
License:	GPL v3+ with BSD parts
Group:		X11/Applications/Publishing
#Source0Download: https://github.com/fontforge/fontforge/releases
Source0:	https://github.com/fontforge/fontforge/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	7043f25368ed25bcd75d168564919fb7
Patch0:		%{name}-po.patch
URL:		https://fontforge.org/
BuildRequires:	cairo-devel >= 1.6
BuildRequires:	cmake >= 3.5
BuildRequires:	freetype-devel >= 1:2.3.7
BuildRequires:	gettext-tools
BuildRequires:	gcc >= 5:3.2
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	gtk+3-devel >= 3.10
BuildRequires:	libbrotli-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libspiro-devel >= 1:0.6
BuildRequires:	libstdc++-devel >= 1:4.7
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libltdl-devel >= 2:2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pango-devel >= 1:1.10
BuildRequires:	pkgconfig >= 1:0.25
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	readline-devel
BuildRequires:	sphinx-pdg
BuildRequires:	tar >= 1:1.22
BuildRequires:	woff2-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	cairo >= 1.6
Requires:	freetype >= 1:2.3.7
Requires:	glib2 >= 1:2.6
Requires:	gtk+3 >= 3.10
Requires:	iconv
Requires:	pango >= 1:1.10
# API and plugins support withdrawn
Obsoletes:	fontforge-devel < 20190413
Obsoletes:	fontforge-static < 20190413
Obsoletes:	pfaedit < 040311
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
Requires:	freetype-devel >= 1:2.3.7
Requires:	giflib-devel
Requires:	libjpeg-devel
Requires:	libltdl-devel
Requires:	libpng-devel
Requires:	libspiro-devel >= 1:0.6
Requires:	libtiff-devel >= 4
Requires:	pango-devel >= 1:1.10
Requires:	xorg-lib-libX11-devel
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

%package -n python3-fontforge
Summary:	Python bindings for FontForge libraries
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek FontForge
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Obsoletes:	python-fontforge < 20200314

%description -n python3-fontforge
Python bindings for FontForge libraries.

%description -n python3-fontforge -l pl.UTF-8
Wiązania Pythona do bibliotek FontForge.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' \
	pycontrib/svg2glyph/svg2glyph

%{__sed} -i -e '1s,/usr/bin/env fontforge,%{_bindir}/fontforge,' \
	pycontrib/simple/expand-a.py \
	pycontrib/simple/load-font-and-show-name.py

# make Sphinx warnings non-fatal
%{__sed} -i -e '/Sphinx_BUILD_BINARY/ s/ -W / /' doc/CMakeLists.txt
# missing?
touch doc/sphinx/contents.rst

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_DOCDIR=%{_docdir}/fontforge \
	%{!?with_doc:-DENABLE_DOCS=OFF} \
	-DENABLE_FONTFORGE_EXTRAS=ON \
%if %{without python}
	-DENABLE_PYTHON_EXTENSION=OFF \
	-DENABLE_PYTHON_SCRIPTING=OFF \
%endif
	-DENABLE_WRITE_PFM=ON

%{__make}

%{__rm} doc/sphinx-docs/{.buildinfo,.nojekyll,objects.inv}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# API no longer exported
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfontforge.so

%{__mv} $RPM_BUILD_ROOT%{_localedir}/ka{_GE,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/tr{_TR,}

%find_lang FontForge

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f FontForge.lang
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%attr(755,root,root) %{_bindir}/acorn2sfd
%attr(755,root,root) %{_bindir}/dewoff
%attr(755,root,root) %{_bindir}/findtable
%attr(755,root,root) %{_bindir}/fontforge
%attr(755,root,root) %{_bindir}/fontimage
%attr(755,root,root) %{_bindir}/fontlint
%attr(755,root,root) %{_bindir}/pcl2ttf
%attr(755,root,root) %{_bindir}/pfadecrypt
%attr(755,root,root) %{_bindir}/rmligamarks
%attr(755,root,root) %{_bindir}/sfddiff
%attr(755,root,root) %{_bindir}/showttf
%attr(755,root,root) %{_bindir}/stripttc
%attr(755,root,root) %{_bindir}/ttf2eps
%attr(755,root,root) %{_bindir}/woff
%attr(755,root,root) %{_libdir}/libfontforge.so.4
%{_datadir}/fontforge
%{_datadir}/metainfo/org.fontforge.FontForge.appdata.xml
%{_datadir}/mime/packages/fontforge.xml
%{_desktopdir}/org.fontforge.FontForge.desktop
%{_iconsdir}/hicolor/*x*/apps/org.fontforge.FontForge.png
%{_iconsdir}/hicolor/scalable/apps/org.fontforge.FontForge.svg
%{_mandir}/man1/acorn2sfd.1*
%{_mandir}/man1/fontforge.1*
%{_mandir}/man1/fontimage.1*
%{_mandir}/man1/fontlint.1*
%{_mandir}/man1/sfddiff.1*
%{_mandir}/man1/showttf.1*
%{_mandir}/man1/ttf2eps.1*

%files doc
%defattr(644,root,root,755)
%dir %{_docdir}/fontforge
%{_docdir}/fontforge/_images
%{_docdir}/fontforge/_static
%{_docdir}/fontforge/appendices
%{_docdir}/fontforge/fontutils
%{_docdir}/fontforge/scripting
%{_docdir}/fontforge/techref
%{_docdir}/fontforge/tutorial
%{_docdir}/fontforge/ui
%dir %{_docdir}/fontforge/old
%lang(de) %{_docdir}/fontforge/old/de
%lang(ja) %{_docdir}/fontforge/old/ja
%{_docdir}/fontforge/*.html
%{_docdir}/fontforge/*.js

%files -n python3-fontforge
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/fontforge.so
%attr(755,root,root) %{py3_sitedir}/psMat.so
