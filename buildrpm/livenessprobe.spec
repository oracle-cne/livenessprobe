

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%global app_name                livenessprobe
%global app_version             2.19.0
%global oracle_release_version  1
%global _buildhost              build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:           %{app_name}
Version:        %{app_version}
Release:        %{oracle_release_version}%{?dist}
Summary:        Sidecar container that exposes an HTTP /healthz endpoint, which serves as kubelet's livenessProbe hook to monitor health of a CSI driver.
License:        Apache 2.0
Group:          Development/Tools
Url:            https://github.com/oracle-cne/livenessprobe.git
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  golang
BuildRequires:	make
Patch0:         build.make.patch

%description
Sidecar container that exposes an HTTP /healthz endpoint, which serves as kubelet's livenessProbe hook to monitor health of a CSI driver.

%prep
%setup -q
%patch0

%build
make build

%install
install -m 755 bin/%{app_name} %{buildroot}/%{app_name}

%files
%license LICENSE THIRD_PARTY_LICENSES.txt olm/SECURITY.md
/%{app_name}

%changelog
* Mon May 25 2026 Oracle Cloud Native Environment Authors <noreply@oracle.com> - 2.19.0-1
- Added Oracle specific build files for CSI livenessprobe.

