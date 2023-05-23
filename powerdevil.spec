#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : powerdevil
Version  : 5.27.5
Release  : 75
URL      : https://download.kde.org/stable/plasma/5.27.5/powerdevil-5.27.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.27.5/powerdevil-5.27.5.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.27.5/powerdevil-5.27.5.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0
Requires: powerdevil-data = %{version}-%{release}
Requires: powerdevil-lib = %{version}-%{release}
Requires: powerdevil-license = %{version}-%{release}
Requires: powerdevil-locales = %{version}-%{release}
Requires: powerdevil-services = %{version}-%{release}
BuildRequires : bluez-qt-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : kactivities-dev
BuildRequires : kded-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kidletime-dev
BuildRequires : kirigami2-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kwayland-dev
BuildRequires : libcap-dev
BuildRequires : libkscreen-dev
BuildRequires : networkmanager-qt-dev
BuildRequires : pkg-config
BuildRequires : plasma-workspace-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the powerdevil package.
Group: Data

%description data
data components for the powerdevil package.


%package dev
Summary: dev components for the powerdevil package.
Group: Development
Requires: powerdevil-lib = %{version}-%{release}
Requires: powerdevil-data = %{version}-%{release}
Provides: powerdevil-devel = %{version}-%{release}
Requires: powerdevil = %{version}-%{release}

%description dev
dev components for the powerdevil package.


%package doc
Summary: doc components for the powerdevil package.
Group: Documentation

%description doc
doc components for the powerdevil package.


%package lib
Summary: lib components for the powerdevil package.
Group: Libraries
Requires: powerdevil-data = %{version}-%{release}
Requires: powerdevil-license = %{version}-%{release}

%description lib
lib components for the powerdevil package.


%package license
Summary: license components for the powerdevil package.
Group: Default

%description license
license components for the powerdevil package.


%package locales
Summary: locales components for the powerdevil package.
Group: Default

%description locales
locales components for the powerdevil package.


%package services
Summary: services components for the powerdevil package.
Group: Systemd services
Requires: systemd

%description services
services components for the powerdevil package.


%prep
%setup -q -n powerdevil-5.27.5
cd %{_builddir}/powerdevil-5.27.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684883893
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1684883893
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/powerdevil
cp %{_builddir}/powerdevil-%{version}/COPYING %{buildroot}/usr/share/package-licenses/powerdevil/7c203dee3a03037da436df03c4b25b659c073976 || :
cp %{_builddir}/powerdevil-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/powerdevil/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang libpowerdevilcommonconfig
%find_lang powerdevil
%find_lang powerdevilactivitiesconfig
%find_lang powerdevilglobalconfig
%find_lang powerdevilprofilesconfig
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kauth/backlighthelper
/V3/usr/lib64/libexec/kauth/chargethresholdhelper
/V3/usr/lib64/libexec/kauth/discretegpuhelper
/V3/usr/lib64/libexec/org_kde_powerdevil
/usr/lib64/libexec/kauth/backlighthelper
/usr/lib64/libexec/kauth/chargethresholdhelper
/usr/lib64/libexec/kauth/discretegpuhelper
/usr/lib64/libexec/org_kde_powerdevil

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_powerdevilactivitiesconfig.desktop
/usr/share/applications/kcm_powerdevilglobalconfig.desktop
/usr/share/applications/kcm_powerdevilprofilesconfig.desktop
/usr/share/dbus-1/system-services/org.kde.powerdevil.backlighthelper.service
/usr/share/dbus-1/system-services/org.kde.powerdevil.chargethresholdhelper.service
/usr/share/dbus-1/system-services/org.kde.powerdevil.discretegpuhelper.service
/usr/share/dbus-1/system.d/org.kde.powerdevil.backlighthelper.conf
/usr/share/dbus-1/system.d/org.kde.powerdevil.chargethresholdhelper.conf
/usr/share/dbus-1/system.d/org.kde.powerdevil.discretegpuhelper.conf
/usr/share/knotifications5/powerdevil.notifyrc
/usr/share/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
/usr/share/polkit-1/actions/org.kde.powerdevil.chargethresholdhelper.policy
/usr/share/polkit-1/actions/org.kde.powerdevil.discretegpuhelper.policy
/usr/share/qlogging-categories5/powerdevil.categories
/usr/share/xdg/autostart/powerdevil.desktop

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libpowerdevilconfigcommonprivate.so
/V3/usr/lib64/libpowerdevilcore.so
/V3/usr/lib64/libpowerdevilui.so
/usr/lib64/libpowerdevilconfigcommonprivate.so
/usr/lib64/libpowerdevilcore.so
/usr/lib64/libpowerdevilui.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/ca/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/de/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/de/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/en/kcontrol/powerdevil/activity.png
/usr/share/doc/HTML/en/kcontrol/powerdevil/advanced.png
/usr/share/doc/HTML/en/kcontrol/powerdevil/energy.png
/usr/share/doc/HTML/en/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/es/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/es/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/et/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/et/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/fr/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/fr/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/id/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/id/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/it/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/it/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/nl/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/nl/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/pt/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/pt/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/pt_BR/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/ru/kcontrol/powerdevil/activity.png
/usr/share/doc/HTML/ru/kcontrol/powerdevil/advanced.png
/usr/share/doc/HTML/ru/kcontrol/powerdevil/energy.png
/usr/share/doc/HTML/ru/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/ru/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/sv/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/tr/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/tr/kcontrol/powerdevil/index.docbook
/usr/share/doc/HTML/uk/kcontrol/powerdevil/activity.png
/usr/share/doc/HTML/uk/kcontrol/powerdevil/advanced.png
/usr/share/doc/HTML/uk/kcontrol/powerdevil/energy.png
/usr/share/doc/HTML/uk/kcontrol/powerdevil/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol/powerdevil/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libpowerdevilconfigcommonprivate.so.5
/V3/usr/lib64/libpowerdevilconfigcommonprivate.so.5.27.5
/V3/usr/lib64/libpowerdevilcore.so.2
/V3/usr/lib64/libpowerdevilcore.so.5.27.5
/V3/usr/lib64/libpowerdevilui.so.5
/V3/usr/lib64/libpowerdevilui.so.5.27.5
/V3/usr/lib64/qt5/plugins/kf5/powerdevil/powerdevilupowerbackend.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_powerdevilactivitiesconfig.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_powerdevilglobalconfig.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_powerdevilprofilesconfig.so
/V3/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_brightnesscontrolaction.so
/V3/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_dimdisplayaction.so
/V3/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_dpmsaction.so
/V3/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_handlebuttoneventsaction.so
/V3/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_keyboardbrightnesscontrolaction.so
/V3/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_powerprofileaction.so
/V3/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_runscriptaction.so
/V3/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_suspendsessionaction.so
/V3/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_wirelesspowersavingaction.so
/V3/usr/lib64/qt5/plugins/powerdevilbrightnesscontrolaction_config.so
/V3/usr/lib64/qt5/plugins/powerdevildimdisplayaction_config.so
/V3/usr/lib64/qt5/plugins/powerdevildpmsaction_config.so
/V3/usr/lib64/qt5/plugins/powerdevilhandlebuttoneventsaction_config.so
/V3/usr/lib64/qt5/plugins/powerdevilkeyboardbrightnesscontrolaction_config.so
/V3/usr/lib64/qt5/plugins/powerdevilpowerprofileaction_config.so
/V3/usr/lib64/qt5/plugins/powerdevilrunscriptaction_config.so
/V3/usr/lib64/qt5/plugins/powerdevilsuspendsessionaction_config.so
/V3/usr/lib64/qt5/plugins/powerdevilwirelesspowersavingaction_config.so
/usr/lib64/libpowerdevilconfigcommonprivate.so.5
/usr/lib64/libpowerdevilconfigcommonprivate.so.5.27.5
/usr/lib64/libpowerdevilcore.so.2
/usr/lib64/libpowerdevilcore.so.5.27.5
/usr/lib64/libpowerdevilui.so.5
/usr/lib64/libpowerdevilui.so.5.27.5
/usr/lib64/qt5/plugins/kf5/powerdevil/powerdevilupowerbackend.so
/usr/lib64/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_powerdevilactivitiesconfig.so
/usr/lib64/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_powerdevilglobalconfig.so
/usr/lib64/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_powerdevilprofilesconfig.so
/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_brightnesscontrolaction.so
/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_dimdisplayaction.so
/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_dpmsaction.so
/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_handlebuttoneventsaction.so
/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_keyboardbrightnesscontrolaction.so
/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_powerprofileaction.so
/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_runscriptaction.so
/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_suspendsessionaction.so
/usr/lib64/qt5/plugins/powerdevil/action/powerdevil_wirelesspowersavingaction.so
/usr/lib64/qt5/plugins/powerdevilbrightnesscontrolaction_config.so
/usr/lib64/qt5/plugins/powerdevildimdisplayaction_config.so
/usr/lib64/qt5/plugins/powerdevildpmsaction_config.so
/usr/lib64/qt5/plugins/powerdevilhandlebuttoneventsaction_config.so
/usr/lib64/qt5/plugins/powerdevilkeyboardbrightnesscontrolaction_config.so
/usr/lib64/qt5/plugins/powerdevilpowerprofileaction_config.so
/usr/lib64/qt5/plugins/powerdevilrunscriptaction_config.so
/usr/lib64/qt5/plugins/powerdevilsuspendsessionaction_config.so
/usr/lib64/qt5/plugins/powerdevilwirelesspowersavingaction_config.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/powerdevil/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/powerdevil/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-powerdevil.service

%files locales -f libpowerdevilcommonconfig.lang -f powerdevil.lang -f powerdevilactivitiesconfig.lang -f powerdevilglobalconfig.lang -f powerdevilprofilesconfig.lang
%defattr(-,root,root,-)

