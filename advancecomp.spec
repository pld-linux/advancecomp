Summary:	Recompression utilities for .ZIP archives, .PNG snapshots, .MNG video clips and .gz files
Summary(pl.UTF-8):	Narzędzia rekompresujące pliki ZIP, PNG, MNG, gz
Name:		advancecomp
Version:	1.15
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://dl.sourceforge.net/advancemame/%{name}-%{version}.tar.gz
# Source0-md5:	bb236d8bee6fa473d34108cda1e09076
URL:		http://advancemame.sourceforge.net/comp-readme.html
BuildRequires:	zlib-devel
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

%build
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
%doc AUTHORS HISTORY README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
