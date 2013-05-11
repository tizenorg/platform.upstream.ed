Name:           ed
Version:        1.6
Release:        1
License:        GPL-3.0+ ; LGPL-2.1+
Summary:        Standard UNIX Line Editor
Url:            http://www.gnu.org/software/ed/
Group:          Productivity/Editors/Other
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The standard, old Unix line editor.

%prep
%setup -q
sed -i \
    -e "s/CFLAGS='.*/CFLAGS='%{optflags}'/" \
    -e "s/CXXFLAGS='.*/CXXFLAGS='%{optflags}'/" \
    configure

%build
%{configure}
make %{?_smp_mflags}

%check
make check

%install
%{makeinstall}

%files
%license COPYING
%defattr(-,root,root)
%{_bindir}/%{name}
%{_bindir}/r%{name}
%doc %{_infodir}/%{name}.info.gz
%doc %{_mandir}/man1/%{name}.1.gz
%doc %{_mandir}/man1/r%{name}.1.gz

