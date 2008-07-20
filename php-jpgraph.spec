%undefine __find_provides
%undefine __find_requires

Summary:	An OO graph drawing class library for PHP5
Name:		php-jpgraph
Version:	2.3.3
Release:	%mkrel 1
License:	QPL
Group:		Networking/Other
URL:		http://www.aditus.nu/jpgraph/
Source0:	http://hem.bredband.net/jpgraph2/jpgraph-%{version}.tar.gz
Requires:	php php-common php-gd gd fonts-ttf-bitstream-vera
BuildArch:	noarch
BuildRequires:	dos2unix
Obsoletes:	php5-jpgraph
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
JpGraph is a OO Graph drawing library for PHP 5.0.x and above.
Highlights of the available features are: text, linear, and log
scales for both the X and Y axes, anti-aliasing of lines,
color-gradient fills, support for GIF, JPG, and PNG formats,
support for two Y axes, spider plots (a.k.a Web plots),
pie-charts, lineplots, filled line plots, impulse plots, bar
plots, and error plots, support for multiple plot types in one
graph, intelligent autoscaling.

Extensive documentations are availible at:
http://www.aditus.nu/jpgraph/

%package	doc
Summary:	Documenation for JpGraph
Group:		Networking/Other

%description	doc
JpGraph is a OO Graph drawing library for PHP 5.0.x and above.
Highlights of the available features are: text, linear, and log
scales for both the X and Y axes, anti-aliasing of lines,
color-gradient fills, support for GIF, JPG, and PNG formats,
support for two Y axes, spider plots (a.k.a Web plots),
pie-charts, lineplots, filled line plots, impulse plots, bar
plots, and error plots, support for multiple plot types in one
graph, intelligent autoscaling.

This package contains the documenation for %{name}.

%prep

%setup -q -n jpgraph-%{version}

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;
find . -type f -perm 0754 -exec chmod 755 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v "\.gif" | grep -v "\.png" | grep -v "\.jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/php-jpgraph
cp -aRf src/* %{buildroot}%{_datadir}/php-jpgraph/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README* 
%dir %{_datadir}/php-jpgraph
%{_datadir}/php-jpgraph/*

%files doc
%defattr(-,root,root)
%doc docs/*
