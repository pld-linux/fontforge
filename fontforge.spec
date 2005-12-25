Summary:	An outline font editor
Summary(pl):	Edytor font�w rysowanych
Name:		fontforge
Version:	20051205
Release:	1
License:	BSD
Group:		X11/Applications/Publishing
Source0:	http://dl.sourceforge.net/fontforge/%{name}_full-%{version}.tar.bz2
# Source0-md5:	d4b766cee54441072d4a2b9db99a2ddf
Patch0:		%{name}-sonames.patch
Patch1:		%{name}-iconv-in-libc.patch
Patch2:		%{name}-sfddiff-build.patch
Patch3:		%{name}-po.patch
URL:		http://fontforge.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
# needed at build time to not disable their support and for detecting SONAME
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libungif-devel
BuildRequires:	libuninameslist-devel
BuildRequires:	libxml2-devel
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
FontForge pozwala na edycj� font�w rysowanych i bitmapowych. Mo�na
tworzy� nowe lub modyfikowa� istniej�ce. Jest to tak�e konwerter
mi�dzy formatami font�w - potrafi obs�ugiwa� fonty postscriptowe
(ASCII i binarne Type 1, cz�� Type 3, cz�� Type 0), TrueType,
OpenType (Type2) i fonty z kluczami CID.

FontForge wcze�niej nazywa� si� PfaEdit.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS LICENSE
%attr(755,root,root) %{_bindir}/fontforge
%attr(755,root,root) %{_bindir}/sfddiff
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*
