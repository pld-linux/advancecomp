#
# Conditional build:
%bcond_with	bzip2	# bzip2 compression
#
Summary:	Recompression utilities for .ZIP archives, .PNG snapshots, .MNG video clips and .gz files
Summary(pl.UTF-8):	Narzędzia rekompresujące pliki ZIP, PNG, MNG, gz
Name:		advancecomp
Version:	1.23
Release:	1
License:	GPL v3+
Group:		Applications/File
Source0:	http://downloads.sourceforge.net/advancemame/%{name}-%{version}.tar.gz
# Source0-md5:	39a205f0ba1baa26550fccc6405a6b45
Patch0:		%{name}-system-libs.patch
URL:		http://advancemame.sourceforge.net/comp-readme.html
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake
%{?with_bzip2:BuildRequires:	bzip2-devel}
BuildRequires:	libdeflate-devel
BuildRequires:	libstdc++-devel
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

%prep
%setup -q
%patch0 -p1

%build
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

%clean
rm -rf $RPM_BUILD_ROOT

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
