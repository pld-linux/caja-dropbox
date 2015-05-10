Summary:	Dropbox extension for Caja file manager
Summary(pl.UTF-8):	Rozszerzenie Dropbox dla zarządcy plików Caja
Name:		caja-dropbox
Version:	1.10.0
Release:	1
License:	GPL v3+ (code), CC-BY-ND v3.0 (images)
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.10/%{name}-%{version}.tar.xz
# Source0-md5:	8c382882e94193fb2e1793dad2441d2c
Patch0:		dropboxd-path.patch
Patch1:		python-gpgme-pkg.patch
URL:		http://getdropbox.com/
BuildRequires:	caja-devel >= 1.1.0
# rst2man
BuildRequires:	docutils
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	pkgconfig
BuildRequires:	python-docutils
BuildRequires:	python-pygtk-gtk >= 2:2
BuildRequires:	python-pygobject >= 2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	caja >= 1.1.0
Requires:	python-modules
Requires:	python-pygtk-gtk >= 2:2
Requires:	xdg-utils
Suggests:	dropbox
Suggests:	python-pygpgme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dropbox extension for Caja file manager, used as sync, versioning and
backup software for your local and remote resources between a number
of machines.

%description -l pl.UTF-8
Rozszerzenie Dropbox dla zarządcy plików Caja, służące do
synchronizacji, obsługi wersji oraz tworzenia kopii zapasowych zasobów
lokalnych oraz zdalnych pomiędzy określonymi maszynami.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%{_datadir}/caja/extensions/libcaja-dropbox.caja-extension
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/emblems
%{_datadir}/%{name}/emblems/*.icon
%{_datadir}/%{name}/emblems/*.png
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/caja-dropbox.png
%{_mandir}/man1/caja-dropbox.1*
