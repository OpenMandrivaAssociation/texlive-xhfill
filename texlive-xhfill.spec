Name:		texlive-xhfill
Version:	22575
Release:	2
Summary:	Extending \hrulefill
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xhfill
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xhfill.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xhfill.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides extended macros for the default \hrulefill
command. It allows modification of the width and the colour of
the line.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xhfill/xhfill.sty
%doc %{_texmfdistdir}/doc/latex/xhfill/Changes
%doc %{_texmfdistdir}/doc/latex/xhfill/Makefile
%doc %{_texmfdistdir}/doc/latex/xhfill/xhfill-doc.pdf
%doc %{_texmfdistdir}/doc/latex/xhfill/xhfill-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
