Summary:	An outline font editor
Summary(pl):	Edytor fontów rysowanych
Name:		fontforge
Version:	20060125
Release:	1
License:	BSD
Group:		X11/Applications/Publishing
Source0:	http://dl.sourceforge.net/fontforge/%{name}_full-%{version}.tar.bz2
# Source0-md5:	831ac5225b1a9b00b0b7bcf622c62fee
Patch0:		%{name}-sonames.patch
Patch1:		%{name}-iconv-in-libc.patch
Patch2:		%{name}-sfddiff-build.patch
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
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-lib-libxkbui-devel

Requires:	iconv
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
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-freetype-bytecode \
	--with-multilayer \
	--without-freetype-src

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

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
%attr(755,root,root) %{_bindir}/sfddiff
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*
