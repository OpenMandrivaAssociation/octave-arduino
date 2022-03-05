%global octpkg arduino

Summary:	Octave Arduino Toolkit
Name:		octave-%{octpkg}
Version:	0.8.0
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel > 4.0.0
BuildRequires:	octave-instrument-control

Requires:	octave(api) = %{octave_api}
Requires:	arduino

Requires(post): octave
Requires(postun): octave

%description
 Basic Octave implementation of the matlab arduino extension, allowing
communication to a programmed arduino board to control its hardware.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -n %{octpkg}-%{version}

%build
export LIBS="-L%{_libdir}"
%set_build_flags
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

