# revision 22575
# category Package
# catalog-ctan /macros/latex/contrib/xhfill
# catalog-date 2011-05-17 17:47:58 +0200
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-xhfill
Version:	1.01
Release:	3
Summary:	Extending \hrulefill
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xhfill
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xhfill.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xhfill.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.01-2
+ Revision: 757657
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.01-1
+ Revision: 719938
- texlive-xhfill
- texlive-xhfill
- texlive-xhfill

