Summary:	Recompression utilities for .ZIP archives, .PNG snapshots, .MNG video clips and .GZ files.
Summary(pl.UTF-8):	Narzędzia rekompresujące pliki zip, png, mng, gz.
Name:		advancecomp
Version:	1.15
Release:	1
License:	GPL
Group:		Applications
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
AdvanceCOMP jest kolekcją narzędzi rekompresujących archiwa zip,
obrazy png, pliki wideo mng i pliki gz.

Ich głównym zastosowaniem jest rekompresja kolekcji rom-ów,
zrzutów ekranu i urywków wideo emulowanych gier.

Głównymi cechami są:
- Rekompresja plików zip, gz, png i mng za pomocą implementacji
  kompresji deflate z 7-Zipa.
- Rekompresja plików mng z użyciem optymalizacji delta i move.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS HISTORY README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
