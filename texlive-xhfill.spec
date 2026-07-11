%global tl_name xhfill
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	Extending \hrulefill
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xhfill
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xhfill.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xhfill.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides extended macros for the default \hrulefill command.
It allows modification of the width and the colour of the line.

