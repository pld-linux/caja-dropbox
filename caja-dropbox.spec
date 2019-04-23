Summary:	Dropbox extension for Caja file manager
Summary(pl.UTF-8):	Rozszerzenie Dropbox dla zarządcy plików Caja
Name:		caja-dropbox
Version:	1.22.1
Release:	1
License:	GPL v3+ (code), CC-BY-ND v3.0 (images)
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.22/%{name}-%{version}.tar.xz
# Source0-md5:	d83e2913454d2b7da026bed377108b50
Patch0:		dropboxd-path.patch
Patch1:		python-gpg-pkg.patch
URL:		http://getdropbox.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	caja-devel >= 1.17.1
# rst2man
BuildRequires:	docutils
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:	python3-docutils
BuildRequires:	python3-pygobject3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	caja >= 1.17.1
Requires:	glib2 >= 1:2.50.0
Requires:	gtk+3
Requires:	python3-pygobject3
Requires:	python3-modules
Requires:	xdg-utils
Suggests:	dropbox
Suggests:	python3-gpg
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
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
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
