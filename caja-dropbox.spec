Summary:	Dropbox extension for Caja
Summary(pl.UTF-8):	Rozszerzenie Dropbox dla Caja
Name:		caja-dropbox
Version:	1.7.90
Release:	2.3
License:	GPL v2 with exceptions
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.7/%{name}-%{version}.tar.xz
# Source0-md5:	877e610ce51f3cc69d8da2daeb58f61d
Patch0:		dropboxd-path.patch
Patch1:		desktop.patch
Patch2:		caja-versions.patch
Patch3:		https://github.com/glensc/caja-dropbox/compare/dl-fixes.patch
URL:		http://getdropbox.com/
BuildRequires:	caja-devel >= 1.1.0
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	libnotify-devel >= 0.4.4
BuildRequires:	pkgconfig
BuildRequires:	python-docutils
BuildRequires:	python-pygtk-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	caja
Requires:	python-modules
Requires:	python-pygtk-gtk
Requires:	xdg-utils
Suggests:	dropbox
Suggests:	python-pygpgme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dropbox extension for Caja used as sync, versioning and backup
software for your local and remote resources between a number of
machines.

%description -l pl.UTF-8
Rozszerzenie Dropbox dla Caja używane do synchronizacji, obsługi
wersji oraz tworzenia kopii zapasowych zasobów lokalnych oraz zdalnych
pomiędzy określonymi maszynami.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-dropbox.so
%{_iconsdir}/hicolor/*/*/*.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/emblems
%{_datadir}/%{name}/emblems/*.icon
%{_datadir}/%{name}/emblems/*.png
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/*.1*
