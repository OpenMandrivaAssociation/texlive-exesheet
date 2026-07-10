%global tl_name exesheet
%global tl_revision 75102

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.9
Release:	%{tl_revision}.1
Summary:	Typesetting exercise or exam sheets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/exesheet
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exesheet.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exesheet.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exesheet.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The exesheet package is designed for typesetting exercise or exam
sheets. The primary advantage of exesheet is its ability to display a
detailed scoring guide and correction instructions as needed. This
feature is especially beneficial for grading papers with multiple
graders. The exesheet package provides: macros for organizing exercises
and subparts, specific settings for enumeration lists, environments for
questions and answers, which can be displayed or hidden, macros for
detailed comments and grading instructions in the margins which can be
displayed or hidden. Additionally, the exesheet class loads the
schooldocs package which manages the page layout, the main title,
headers and footers.

