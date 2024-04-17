#
# Conditional build:
%bcond_with	bzip2	# bzip2 compression
#
Summary:	Recompression utilities for .ZIP archives, .PNG snapshots, .MNG video clips and .gz files
Summary(pl.UTF-8):	Narzędzia rekompresujące pliki ZIP, PNG, MNG, gz
Name:		advancecomp
Version:	2.6
Release:	1
License:	GPL v3+
Group:		Applications/File
#Source0Download: https://github.com/amadvance/advancecomp/releases
Source0:	https://github.com/amadvance/advancecomp/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fc7f6c2bdbabae26f90bf18ec63e9242
Patch0:		%{name}-system-libs.patch
Patch1:		%{name}-7z-lib.patch
URL:		http://www.advancemame.it/comp-readme.html
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake
%{?with_bzip2:BuildRequires:	bzip2-devel}
BuildRequires:	libdeflate-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	zlib-devel
BuildRequires:	zopfli-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AdvanceCOMP is a collection of recompression utilities for your .ZIP
archives, .PNG snapshots, .MNG video clips and .GZ files.

It's mainly intended for recompressing your rom, snapshot and clip
collection of emulated games.

The main features are:
- Recompress ZIP, GZ, PNG and MNG files using the Deflate 7-Zip
  implementation.
- Recompress MNG files using Delta and Move optimization. 

%description -l pl.UTF-8
AdvanceCOMP jest kolekcją narzędzi rekompresujących archiwa ZIP,
obrazy PNG, pliki wideo MNG i pliki gz.

Ich głównym zastosowaniem jest rekompresja kolekcji ROM-ów,
zrzutów ekranu i urywków wideo emulowanych gier.

Głównymi cechami są:
- Rekompresja plików ZIP, gz, PNG i MNG za pomocą implementacji
  kompresji deflate z 7-Zipa.
- Rekompresja plików MNG z użyciem optymalizacji delta i move.

%package 7z
Summary:	7z library from AdvanceCOMP project
Summary(pl.UTF-8):	Biblioteka 7z z projektu AdvanceCOMP
Group:		Libraries

%description 7z
7z library from AdvanceCOMP project.

%description 7z -l pl.UTF-8
Biblioteka 7z z projektu AdvanceCOMP.

%package 7z-devel
Summary:	Header file for AdvanceCOMP 7z library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki AdvanceCOMP 7z
Group:		Development/Libraries
Requires:	%{name}-7z = %{version}-%{release}
Requires:	libstdc++-devel

%description 7z-devel
Header file for AdvanceCOMP 7z library.

%description 7z-devel -l pl.UTF-8
Plik nagłówkowy biblioteki AdvanceCOMP 7z.

%package 7z-static
Summary:	Static AdvanceCOMP 7z library
Summary(pl.UTF-8):	Statyczna biblioteka AdvanceCOMP 7z
Group:		Development/Libraries
Requires:	%{name}-7z-devel = %{version}-%{release}

%description 7z-static
Static AdvanceCOMP 7z library.

%description 7z-static -l pl.UTF-8
Statyczna biblioteka AdvanceCOMP 7z.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_bzip2:--enable-bzip2}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libadv7z.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	7z -p /sbin/ldconfig
%postun	7z -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS HISTORY README
%attr(755,root,root) %{_bindir}/advdef
%attr(755,root,root) %{_bindir}/advmng
%attr(755,root,root) %{_bindir}/advpng
%attr(755,root,root) %{_bindir}/advzip
%{_mandir}/man1/advdef.1*
%{_mandir}/man1/advmng.1*
%{_mandir}/man1/advpng.1*
%{_mandir}/man1/advzip.1*

%files 7z
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libadv7z.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libadv7z.so.0

%files 7z-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libadv7z.so
%{_includedir}/adv7z

%files 7z-static
%defattr(644,root,root,755)
%{_libdir}/libadv7z.a
