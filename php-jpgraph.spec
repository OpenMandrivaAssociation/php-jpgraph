%undefine __find_provides
%undefine __find_requires

Summary:	An OO graph drawing class library for PHP5
Name:		php-jpgraph
Version:	2.3.3
Release:	%mkrel 4
License:	QPL
Group:		Networking/Other
URL:		http://www.aditus.nu/jpgraph/
Source0:	http://hem.bredband.net/jpgraph2/jpgraph-%{version}.tar.gz
Requires:	gd
Requires:	php-gd
Requires:	fonts-ttf-bitstream-vera
BuildArch:	noarch
Obsoletes:	php5-jpgraph
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/php/jpgraph
install -m 644 src/*.php %{buildroot}%{_datadir}/php/jpgraph
install -m 644 src/*.dat %{buildroot}%{_datadir}/php/jpgraph
install -d -m 755 %{buildroot}%{_datadir}/php/jpgraph/lang
install -m 644 src/lang/*.php %{buildroot}%{_datadir}/php/jpgraph/lang

install -d -m 755 %{buildroot}%{_docdir}/%{name}
cp -r docs %{buildroot}%{_docdir}/%{name}
cp -r src/Examples %{buildroot}%{_docdir}/%{name}
install -m 644 README VERSION QPL.txt %{buildroot}%{_docdir}/%{name}
install -m 644 src/CHANGELOG-2.3.3.txt %{buildroot}%{_docdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_docdir}/%{name}
%{_datadir}/php/jpgraph
%exclude %{_docdir}/%{name}/Examples
%exclude %{_docdir}/%{name}/docs

%files doc
%defattr(-,root,root)
%{_docdir}/%{name}/Examples
%{_docdir}/%{name}/docs
