%global debug_package %{nil}

Name: python-alabaster
Epoch: 100
Version: 0.7.12
Release: 1%{?dist}
BuildArch: noarch
Summary: Lightweight, configurable Sphinx theme
License: BSD-3-Clause
URL: https://github.com/bitprophet/alabaster/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Alabaster is a visually (c)lean, responsive, configurable theme for the
Sphinx documentation system. It is Python 2+3 compatible.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-alabaster
Summary: Lightweight, configurable Sphinx theme
Requires: python3
Provides: python3-alabaster = %{epoch}:%{version}-%{release}
Provides: python3dist(alabaster) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-alabaster = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(alabaster) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-alabaster = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(alabaster) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-alabaster
Alabaster is a visually (c)lean, responsive, configurable theme for the
Sphinx documentation system. It is Python 2+3 compatible.

%files -n python%{python3_version_nodots}-alabaster
%license LICENSE
%{python3_sitelib}/alabaster*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-alabaster
Summary: Lightweight, configurable Sphinx theme
Requires: python3
Provides: python3-alabaster = %{epoch}:%{version}-%{release}
Provides: python3dist(alabaster) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-alabaster = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(alabaster) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-alabaster = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(alabaster) = %{epoch}:%{version}-%{release}

%description -n python3-alabaster
Alabaster is a visually (c)lean, responsive, configurable theme for the
Sphinx documentation system. It is Python 2+3 compatible.

%files -n python3-alabaster
%license LICENSE
%{python3_sitelib}/alabaster*
%endif

%changelog
