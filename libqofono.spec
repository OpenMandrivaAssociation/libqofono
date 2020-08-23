%define debug_package %{nil}
%define major %(echo %{version} |cut -d. -f1)

%define libname %mklibname qofono-qt5 %{major}
%define devname %mklibname -d qofono-qt5

Summary:	Library for accessing the oFono phone system through Qt and QtQuick
Name:		libqofono
Version:	0.100
Release:	1
Source0:	https://git.sailfishos.org/mer-core/libqofono/-/archive/%{version}/libqofono-%{version}.tar.bz2
BuildRequires:	pkgconfig(ofono)
BuildRequires:	qmake5
BuildRequires:	make
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(dbus-1)
License:	LGPLv2.1

%description
A library for accessing the ofono daemon, and a declarative plugin for it.
This allows accessing ofono in qtquick and friends.

%package -n %{libname}
Summary:	Library for accessing the oFono phone system through Qt and QtQuick

%description -n %{libname}
A library for accessing the ofono daemon, and a declarative plugin for it.
This allows accessing ofono in qtquick and friends.

%package -n %{devname}
Summary:	Development files for libqofono-qt5
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
A library for accessing the ofono daemon, and a declarative plugin for it.
This allows accessing ofono in qtquick and friends.

This package contains files needed to develop applications using libqofono.

%package examples
Summary:	Examples for libqofono-qt5
Requires:	%{libname} = %{EVRD}

%description examples
A library for accessing the ofono daemon, and a declarative plugin for it.
This allows accessing ofono in qtquick and friends.

This package contains examples showing how to use libqofono.

%package tests
Summary:	Tests for libqofono-qt5
Requires:	%{libname} = %{EVRD}

%description tests
A library for accessing the ofono daemon, and a declarative plugin for it.
This allows accessing ofono in qtquick and friends.

This package contains tests for libqofono.

%prep
%autosetup -p1
qmake-qt5 *.pro

%build
%make_build

%install
%make_build install INSTALL_ROOT=%{buildroot}
mv %{buildroot}/opt/examples/libqofono-qt5 %{buildroot}%{_libdir}/libqofono-qt5/examples
mv %{buildroot}/opt/tests/* %{buildroot}%{_libdir}/libqofono-qt5/tests

# Fix naming and move to the right place...
mkdir -p %{buildroot}%{_datadir}/dbus-1/interfaces
cd %{buildroot}%{_includedir}/qofono-qt5/dbus
sed -i -e 's, name="",,g' *.xml
for i in *.xml; do
	N=$(grep '<interface ' $i |cut -d'"' -f2)
	mv $i %{buildroot}%{_datadir}/dbus-1/interfaces/$N.xml
done

%files -n %{libname}
%{_libdir}/libqofono-qt5.so.%{major}*
%{_libdir}/qt5/qml/MeeGo/QOfono
%{_datadir}/dbus-1/interfaces/*.xml

%files -n %{devname}
%dir %{_includedir}/qofono-qt5
%{_includedir}/qofono-qt5/*.h
%{_libdir}/libqofono-qt5.prl
%{_libdir}/libqofono-qt5.so
%{_libdir}/pkgconfig/qofono-qt5.pc
%{_libdir}/qt5/share/qt5/mkspecs/features/qofono-qt5.prf

%files examples
%dir %{_libdir}/libqofono-qt5
%{_libdir}/libqofono-qt5/examples

%files tests
%dir %{_libdir}/libqofono-qt5
%{_libdir}/libqofono-qt5/tests
