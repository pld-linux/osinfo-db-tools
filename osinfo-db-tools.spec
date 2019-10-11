Summary:	Tools for managing the osinfo database
Summary(pl.UTF-8):	Narzędzia do zarządzania bazą danych osinfo
Name:		osinfo-db-tools
Version:	1.6.0
Release:	1
License:	GPL v2+
Group:		Applications/File
Source0:	https://releases.pagure.org/libosinfo/%{name}-%{version}.tar.gz
# Source0-md5:	edfb599f960161d348c67f3261627136
URL:		https://libosinfo.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	json-glib-devel
BuildRequires:	libarchive-devel >= 3.0.0
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libtool >= 2:2
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	libxslt-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	xz
Requires:	glib2 >= 1:2.44
Requires:	libarchive >= 3.0.0
Requires:	libxml2 >= 1:2.6.0
Requires:	libxslt >= 1.0.0
Conflicts:	libosinfo < 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization.

%description -l pl.UTF-8
Ten pakiet dostarcza narzędzia do zarządzania bazą danych osinfo,
zawierającą informacje o systemach operacyjnych przeznaczone do
wykorzystania przy wirtualizacji.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{bal,ilo,kw@kkcor,kw@uccor,wba}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README docs/*.txt
%attr(755,root,root) %{_bindir}/osinfo-db-export
%attr(755,root,root) %{_bindir}/osinfo-db-import
%attr(755,root,root) %{_bindir}/osinfo-db-path
%attr(755,root,root) %{_bindir}/osinfo-db-validate
%{_mandir}/man1/osinfo-db-export.1*
%{_mandir}/man1/osinfo-db-import.1*
%{_mandir}/man1/osinfo-db-path.1*
%{_mandir}/man1/osinfo-db-validate.1*
