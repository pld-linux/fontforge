Summary:	An outline font editor
Summary(pl.UTF-8):	Edytor fontów rysowanych
Name:		fontforge
Version:	20090923
Release:	4
License:	BSD
Group:		X11/Applications/Publishing
Source0:	http://dl.sourceforge.net/fontforge/%{name}_full-%{version}.tar.bz2
# Source0-md5:	ea9d8dc38de79235fbe6add725b38ffe
Patch0:		%{name}-sonames.patch
Patch1:		%{name}-libpng.patch
URL:		http://fontforge.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
# needed at build time to not disable their support and for detecting SONAME
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libuninameslist-devel
BuildRequires:	libxml2-devel
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
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

%prep
%setup -q
# hardcoded in code is +- same as hardcoded at compile time
#%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--enable-type3 \
	--enable-devicetables \
	--enable-longdouble \
	--with-freetype-bytecode \
	--with-regular-link \
	--without-freetype-src

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

# Malayalam is ml
mv $RPM_BUILD_ROOT%{_datadir}/locale/m{a,}l

%find_lang FontForge

rm -rf $RPM_BUILD_ROOT%{_libdir}/{*.la,pkgconfig}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f FontForge.lang
%defattr(644,root,root,755)
%doc AUTHORS LICENSE
%attr(755,root,root) %{_bindir}/fontforge
%attr(755,root,root) %{_bindir}/fontimage
%attr(755,root,root) %{_bindir}/fontlint
%attr(755,root,root) %{_bindir}/sfddiff
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_datadir}/fontforge
%{_mandir}/man1/*
