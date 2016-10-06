%global debug_package %{nil}

Name:		polychromatic
Version:	0.2.3
Release:	1%{?dist}
Summary:	A graphical front end to manage Razer perihperals on GNU/Linux.

License:	GPLv2
URL:		https://github.com/lah7/polychromatic
Source0:	https://github.com/lah7/polychromatic/archive/v%{version}.tar.gz

BuildRequires:	python3-devel
BuildRequires:	rsync

Requires:	python-razer-chroma-libs
Requires:	python3-setproctitle
Requires:	python3-gobject
Requires:	libappindicator
Requires:	libappindicator-gtk3
Requires:	webkitgtk


%description
A graphical front end to manage your Razer perihperals on GNU/Linux.
Powered by the Chroma Linux Drivers daemon.


%prep
%setup -q

%build
# Nothing to build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_datadir}/%{name}
install -m 0644 LICENSE README.md %{buildroot}/%{_datadir}/%{name}
cp -r data/* %{buildroot}/%{_datadir}/%{name}

mkdir -p %{buildroot}/%{_bindir}
install -m 0755 polychromatic-controller polychromatic-tray-applet %{buildroot}/%{_bindir}

mkdir -p %{buildroot}/%{python3_sitelib}/polychromatic
install -m 0644 pylib/*.py %{buildroot}/%{python3_sitelib}/polychromatic

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps
install -m 0644 "install/hicolor/scalable/apps/polychromatic.svg" %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps

mkdir -p %{buildroot}/%{_datadir}/applications
install -m 0644 "install/polychromatic-controller.desktop" %{buildroot}/%{_datadir}/applications
install -m 0644 "install/polychromatic-tray-applet.desktop" %{buildroot}/%{_datadir}/applications

mkdir -p %{buildroot}/%{_datadir}/locale
rsync -rlpt --exclude="polychromatic-controller.pot" --exclude="polychromatic-tray-applet.pot" --exclude=*.po locale/ %{buildroot}/%{_datadir}/locale

%files
%doc LICENSE README.md
%{_bindir}/polychromatic-controller
%{_bindir}/polychromatic-tray-applet
%{python3_sitelib}/polychromatic
%{_datadir}/icons/hicolor/scalable/apps/polychromatic.svg
%{_datadir}/applications/polychromatic-controller.desktop
%{_datadir}/applications/polychromatic-tray-applet.desktop
%{_datadir}/locale/
%{_datadir}/polychromatic/


%changelog
* Thu Aug 18 2016 Michael Donnelly <mike@donnellyonline.com> 0.2.3-1
- Initial RPM
