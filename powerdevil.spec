#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v19
# autospec commit: f35655a
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : powerdevil
Version  : 6.1.5
Release  : 98
URL      : https://download.kde.org/stable/plasma/6.1.5/powerdevil-6.1.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.1.5/powerdevil-6.1.5.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.1.5/powerdevil-6.1.5.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
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
BuildRequires : gnupg
BuildRequires : kded-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kidletime-dev
BuildRequires : kirigami-dev
BuildRequires : knotifyconfig-dev
BuildRequires : layer-shell-qt-dev
BuildRequires : libcap-dev
BuildRequires : libkscreen-dev
BuildRequires : pkg-config
BuildRequires : plasma-activities-dev
BuildRequires : plasma-workspace-dev
BuildRequires : qt6base-dev
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: noautosuspend.patch

%description
# PowerDevil
PowerDevil is the internal name of the KDE power management service for Plasma.
It is responsible for some (but not all) interactions with hardware functionality. The service will:

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n powerdevil-6.1.5
cd %{_builddir}/powerdevil-6.1.5
%patch -P 1 -p1
pushd ..
cp -a powerdevil-6.1.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726013358
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1726013358
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/powerdevil
cp %{_builddir}/powerdevil-%{version}/COPYING %{buildroot}/usr/share/package-licenses/powerdevil/7c203dee3a03037da436df03c4b25b659c073976 || :
cp %{_builddir}/powerdevil-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/powerdevil/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/powerdevil-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/powerdevil/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/powerdevil-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/powerdevil/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/powerdevil-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/powerdevil/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/powerdevil-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/powerdevil/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/powerdevil-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/powerdevil/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/powerdevil-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/powerdevil/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/powerdevil-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/powerdevil/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/powerdevil-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/powerdevil/19d98e1b6f8ef12849ea4012a052d3907f336c91 || :
cp %{_builddir}/powerdevil-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/powerdevil/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/powerdevil-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/powerdevil/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/powerdevil-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/powerdevil/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/powerdevil-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/powerdevil/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kcm_powerdevilprofilesconfig
%find_lang libpowerdevilcommonconfig
%find_lang powerdevil
%find_lang powerdevil_osd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf6/kauth/backlighthelper
/V3/usr/lib64/libexec/kf6/kauth/chargethresholdhelper
/V3/usr/lib64/libexec/kf6/kauth/discretegpuhelper
/V3/usr/lib64/libexec/org_kde_powerdevil
/V3/usr/lib64/libexec/power_profile_osd_service
/usr/lib64/libexec/kf6/kauth/backlighthelper
/usr/lib64/libexec/kf6/kauth/chargethresholdhelper
/usr/lib64/libexec/kf6/kauth/discretegpuhelper
/usr/lib64/libexec/org_kde_powerdevil
/usr/lib64/libexec/power_profile_osd_service

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_powerdevilprofilesconfig.desktop
/usr/share/dbus-1/services/org.kde.powerdevil.powerProfileOsdService.service
/usr/share/dbus-1/system-services/org.kde.powerdevil.backlighthelper.service
/usr/share/dbus-1/system-services/org.kde.powerdevil.chargethresholdhelper.service
/usr/share/dbus-1/system-services/org.kde.powerdevil.discretegpuhelper.service
/usr/share/dbus-1/system.d/org.kde.powerdevil.backlighthelper.conf
/usr/share/dbus-1/system.d/org.kde.powerdevil.chargethresholdhelper.conf
/usr/share/dbus-1/system.d/org.kde.powerdevil.discretegpuhelper.conf
/usr/share/knotifications6/powerdevil.notifyrc
/usr/share/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
/usr/share/polkit-1/actions/org.kde.powerdevil.chargethresholdhelper.policy
/usr/share/polkit-1/actions/org.kde.powerdevil.discretegpuhelper.policy
/usr/share/qlogging-categories6/powerdevil.categories
/usr/share/xdg/autostart/powerdevil.desktop

%files dev
%defattr(-,root,root,-)
/usr/lib64/libpowerdevilconfigcommonprivate.so
/usr/lib64/libpowerdevilcore.so

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
/V3/usr/lib64/libpowerdevilconfigcommonprivate.so.6.1.5
/V3/usr/lib64/libpowerdevilcore.so.6.1.5
/V3/usr/lib64/qt6/plugins/plasma/kcms/systemsettings/kcm_powerdevilprofilesconfig.so
/V3/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_brightnesscontrolaction.so
/V3/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_dimdisplayaction.so
/V3/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_dpmsaction.so
/V3/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_handlebuttoneventsaction.so
/V3/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_keyboardbrightnesscontrolaction.so
/V3/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_powerprofileaction.so
/V3/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_runscriptaction.so
/V3/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_suspendsessionaction.so
/usr/lib64/libpowerdevilconfigcommonprivate.so.6
/usr/lib64/libpowerdevilconfigcommonprivate.so.6.1.5
/usr/lib64/libpowerdevilcore.so.2
/usr/lib64/libpowerdevilcore.so.6.1.5
/usr/lib64/qt6/plugins/plasma/kcms/systemsettings/kcm_powerdevilprofilesconfig.so
/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_brightnesscontrolaction.so
/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_dimdisplayaction.so
/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_dpmsaction.so
/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_handlebuttoneventsaction.so
/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_keyboardbrightnesscontrolaction.so
/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_powerprofileaction.so
/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_runscriptaction.so
/usr/lib64/qt6/plugins/powerdevil/action/powerdevil_suspendsessionaction.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/powerdevil/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/powerdevil/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/powerdevil/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/powerdevil/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/powerdevil/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/powerdevil/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/powerdevil/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/powerdevil/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/powerdevil/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/powerdevil/e458941548e0864907e654fa2e192844ae90fc32

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-powerdevil.service
/usr/lib/systemd/user/plasma-powerprofile-osd.service

%files locales -f kcm_powerdevilprofilesconfig.lang -f libpowerdevilcommonconfig.lang -f powerdevil.lang -f powerdevil_osd.lang
%defattr(-,root,root,-)

