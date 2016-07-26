Name:           pmacct
Version:        1.6.0
Release:        1%{?dist}
Summary:        passive network monitoring

License:        GPLv2
URL:            http://www.pmacct.net/
Source0:        http://www.pmacct.net/pmacct-%{version}.tar.gz

BuildRequires:  sqlite-devel, libpcap-devel, zlib-devel

%description
pmacct is a small set of multi-purpose passive network monitoring tools

%prep
%setup -q

%build
%configure --enable-sqlite3
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -type f | sed 's|^%{buildroot}||' > filelist

%files -f filelist

%changelog
* Tue Jul 26 2016 Davide Principi <davide.principi@nethesis.it>
- Initial version
