Summary:	Library handling GDB/MI interface
Summary(pl.UTF-8):	Biblioteka obsługująca interfejs GDB/MI
Name:		libmigdb
Version:	0.8.11
Release:	1
License:	GPL v2
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/libmigdb/%{name}-%{version}.tar.bz2
# Source0-md5:	436484fe32f552f28ac06f16828c21b8
URL:		http://sourceforge.net/projects/libmigdb/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is an attempt to support the GDB/MI interface. MI stands
for machine interface. In this mode gdb sends responses that are
"machine readable" instead of "human readable".

%description -l pl.UTF-8
Ta biblioteka jest próbą obsługi interfejsu GDB/MI. MI oznacza
interfejs maszyny. W tym trybie gdb wysyła odpowiedzi, które są
"zrozumiałe dla maszyny" zamiast "zrozumiałych dla człowieka".

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

install src/libmigdb.a $RPM_BUILD_ROOT%{_libdir}
install src/mi_gdb.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc change.log README doc/reference.html
%{_includedir}/*
%{_libdir}/*
