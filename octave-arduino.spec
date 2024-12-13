%global octpkg arduino

Summary:	Octave Arduino Toolkit
Name:		octave-arduino
Version:	0.12.1
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/arduino/
Source0:	https://downloads.sourceforge.net/octave/arduino-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:  octave-instrument-control >= 0.5.0

Requires:	arduino
Requires:	octave(api) = %{octave_api}
Requires:  	octave-instrument-control >= 0.5.0

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Basic Octave implementation of the matlab arduino extension, allowing
communication to a programmed arduino board to control its hardware.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

