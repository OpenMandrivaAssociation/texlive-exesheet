Name:		texlive-exesheet
Version:	68692
Release:	1
Summary:	Typesetting exercise or exam sheets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exesheet
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exesheet.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exesheet.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exesheet.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is used for typesetting exercise or exam sheets.
In addition, the exesheet class loads the schooldocs package.
The package provides: macros to mark out exercises and
subparts, specific settings for enumeration lists, environments
for questions and answers, with conditional display, macros for
marking schemes with detailed comments.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/exesheet
%{_texmfdistdir}/tex/latex/exesheet
%doc %{_texmfdistdir}/doc/latex/exesheet

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
