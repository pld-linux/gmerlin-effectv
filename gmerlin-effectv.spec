Summary:	EffecTV effects ported to gmerlin
Summary(pl.UTF-8):	Efekty z projektu EffecTV przeportowane do gmerlina
Name:		gmerlin-effectv
Version:	1.2.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/gmerlin/%{name}-%{version}.tar.gz
# Source0-md5:	f8bc379f6678dff2aa89dbfc4e5ee0b4
Patch0:		%{name}-am.patch
URL:		http://gmerlin.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gmerlin-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	gmerlin >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains most effects from EffecTV
(http://effectc.sourceforge.net/) ported to gmerlin. Missing Effects
are mostly the ones, which do things, which cannot be done within a
generic filter API.

%description -l pl.UTF-8
Ten pakiet zawiera większość efektów z projektu EffecTV
(http://effectc.sourceforge.net/) przeportowanych do gmerlina.
Brakujące efekty to głównie wykonujące rzeczy, których nie można
zrobić poprzez ogólne API filtrów.

%prep
%setup -q
%patch0 -p1

# evil, sets CFLAGS basing on /proc/cpuinfo, overrides our optflags
# (--with-cpuflags=none disables using /proc/cpuinfo, but not overriding)
sed -i -e '19,$d;18aAC_DEFUN([LQT_OPT_CFLAGS],[OPT_CFLAGS="$CFLAGS"])' m4/lqt_opt_cflags.m4

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened plugins
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gmerlin/plugins/*.la

# just empty file
#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/gmerlin/plugins/fv_*tv.so
