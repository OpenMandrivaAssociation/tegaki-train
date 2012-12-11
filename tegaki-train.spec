Summary: 	Character editor and training manager
Name: 		tegaki-train
Version: 	0.3.1
Release: 	%mkrel 1
License: 	GPLv2+
Group: 		System/Internationalization
Source: 	http://www.tegaki.org/releases/%version/%name-%version.tar.gz
URL: 		http://www.tegaki.org
Buildroot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	python-setuptools
Requires:	tegaki-pygtk
BuildArch:	noarch

%description
Tegaki is an ongoing project which aims to develop a free and open-source
modern implementation of handwriting recognition software, that is suitable for
both the desktop and mobile devices, and that is designed from the ground up to
work well with Chinese and Japanese.

%prep
%setup -qn %name-%version

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%{_bindir}/*
%{py_puresitedir}/tegaki*


%changelog
* Wed Nov 03 2010 Funda Wang <fwang@mandriva.org> 0.3.1-1mdv2011.0
+ Revision: 592784
- import tegaki-train

