Summary:	Tools for managing the osinfo database
Name:		osinfo-db-tools
Version:	1.1.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://releases.pagure.org/libosinfo/%{name}-%{version}.tar.gz
# Source0-md5:	5b346d7e361a7f510aa62da923cbdd8b
URL:		https://libosinfo.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gnome-common
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libarchive-devel >= 3.0.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	libxslt-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/osinfo-db-export
%attr(755,root,root) %{_bindir}/osinfo-db-import
%attr(755,root,root) %{_bindir}/osinfo-db-path
%attr(755,root,root) %{_bindir}/osinfo-db-validate
%{_mandir}/man1/osinfo-db-export.1*
%{_mandir}/man1/osinfo-db-import.1*
%{_mandir}/man1/osinfo-db-path.1*
%{_mandir}/man1/osinfo-db-validate.1*

