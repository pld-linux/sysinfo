Summary:	Sysinfo - know your computer
Summary(pl):	Sysinfo - znaj sw�j komputer
Name:		sysinfo
Version:	0.6.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sf.net/gsysinfo/%{name}-%{version}.tar.bz2
# Source0-md5:	bc4b17c2ce0193f22d41602f6640ed6d
URL:		http://sysinfo.r8.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkmm-devel
BuildRequires:	libglademm-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sysinfo is a simple GNU/Linux program which can display some
computer/system information:

- General information: Kernel version, Distribution release,
  Hostname/domainname, some important software versions,
- CPU information: Name/vendor, Frequency, L2 Cache,
  model/family/stepping,
- Memory information: Total, Free, Cached, Active/inactive, Swap,
- IDE information: Disks, CD/DVD-roms, Model, Capacity, Cache,
- Filesystem information: Filesystem disk space usage(mounted
  partitions),
- Hardware information: Motherboard chipset, IDE interface, VGA
  contoller, Multimedia controllers(sound cards), Ethernet cards,
- USB information: USB controllers,
- NVIDIA information: Graphic card model, AGP rate, Fast writes/SBA,
  Driver version,
- Other information: Sound card details, Input devices, Screen
  resolution.

%description -l pl
Sysinfo jest prostym linuksowym programem wy�wietlaj�cym informacje o
komputerze/systemie:

- Og�lne informacje: wersja j�dra, wersja dystrybucji, nazwa
  hosta/domeny, wersje wa�niejszych program�w,
- Informacje o procesorze: nazwa/producent, cz�stotliwo��, cache L2,
  model/rodzina/stepping,
- Informacje o pami�ci: ilo�� ca�kowita, wolna, cache,
  aktywna/nieaktywna, swap.
- Informacje o IDE: dyski, CD/DVD-romy, modele, pojemno�ci, cache,
- Informacje o systemach plik�w: ilo�� wolnego miejsca,
- Informacje o sprz�cie: mostek na p�ycie g��wnej, interfejs IDE,
  kontroler VGA, kontrolery multimedi�w (karty d�wi�kowe), karty
  sieciowe,
- Informacje o USB: kontrolery USB,
- Informacje o NVIDII: model karty graficznej, mno�nik AGP, Fast
  writes/SBA, wersja sterownika,
- Inne informacje: szczeg�y karty d�wi�kowej, urz�dze� wej�cia,
  rozdzielczo�� obrazu.

%prep
%setup -q

%build
%{__aclocal}
%{__libtoolize}
%{__autoconf}
%{__automake}
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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/sysinfo
%{_desktopdir}/*
%{_pixmapsdir}/sysinfo
