Summary:	TurboC - a library for porting Borland Turbo C to GNU gcc
Summary(pl):	TurboC - biblioteka do portowania Turbo C Borlanda do GNU gcc
Name:		TurboC
Version:	20021216
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://www.sandroid.org/TurboC/%{name}-dev.tar.gz
# Source0-md5:	817209a0d40a02fa44a649dbe5ed022f
Patch0:		%{name}-memset.patch
URL:		http://www.sandroid.org/TurboC/
BuildRequires:	XFree86-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/TurboC

%description
TurboC is a useful little kit of stuff that can be used for converting
a Borland Turbo C application to a GNU gcc program. It doesn't do the
whole job, but it does provide various library functions present in
Turbo C but not in gcc libraries.

It contains replacements for the following headers: alloc.h bios.h
dir.h dos.h fnkeys.h graphics.h io.h.

%description -l pl
TurboC to zestaw przydatny do konwersji program�w z Turbo C Borlanda
do GNU gcc. Nie wykonuje ca�ej pracy, ale dostarcza r�nych funkcji
obecnych w Turbo C, kt�rych nie ma w gcc.

Zawiera zamienniki nast�puj�cych plik�w nag��wkowych: alloc.h bios.h
dir.h dos.h fnkeys.h graphics.h io.h.

%prep
%setup -q -n %{name}-source
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	COPTIONS="%{rpmcflags} -DWITH_X -I/usr/X11R6/include -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

install *.a $RPM_BUILD_ROOT%{_libdir}
install TurboC.h alloc.h bios.h dir.h dos.h fnkeys.h graphics.h io.h \
	$RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}
