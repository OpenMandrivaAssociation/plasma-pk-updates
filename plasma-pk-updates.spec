Name:		plasma-pk-updates
Version:	0.3.2
Release:	1
Summary:	Plasma applet for system updates using PackageKit
License:	GPLv2+
URL:		https://cgit.kde.org/plasma-pk-updates.git
# Git snapshot
# git clone git://anongit.kde.org/plasma-pk-updates.git; cd plasma-pk-updates
# git archive --prefix=plasma-pk-updates-%{version}/ %{commit0} | xz -9 > ../plasma-pk-updates-%{version}-%{shortcommit0}.tar.xz
Source0:	https://github.com/KDE/plasma-pk-updates/archive/v%{version}.tar.gz

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Declarative)
BuildRequires:	pkgconfig(packagekitqt5)
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	packagekit
BuildRequires:	ninja

%description
Plasma applet for system updates using PackageKit

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.pkupdates.desktop
%{_libdir}/qt5/qml/org/kde/plasma/PackageKit
%{_datadir}/plasma/plasmoids/org.kde.plasma.pkupdates/
%{_datadir}/metainfo/org.kde.plasma.pkupdates.appdata.xml
