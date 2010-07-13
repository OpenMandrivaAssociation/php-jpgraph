%undefine __find_provides
%undefine __find_requires

Summary:	An OO graph drawing class library for PHP5
Name:		php-jpgraph
Version:	3.0.7
Release:	%mkrel 1
License:	QPL
Group:		Networking/Other
URL:		http://jpgraph.net/
Source0:	http://hem.bredband.net/jpgraph2/jpgraph-%{version}.tar.bz2
Patch0:		jpgraph-3.0.6-CVE-2009-4422.diff
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

Extensive documentations are available at:
http://jpgraph.net/doc/

%package	doc
Summary:	Documentation for JpGraph
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

This package contains the documentation for %{name}.

%prep
%setup -q -c -n jpgraph-%{version}
%patch0 -p0

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/php/jpgraph
cp -aRf src/* %{buildroot}%{_datadir}/php/jpgraph/

install -d -m 755 %{buildroot}%{_docdir}/%{name}
cp -r docportal %{buildroot}%{_docdir}/%{name}
cp -r src/Examples %{buildroot}%{_docdir}/%{name}
install -m 644 README VERSION %{buildroot}%{_docdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_docdir}/%{name}
%{_datadir}/php/jpgraph
%exclude %{_docdir}/%{name}/Examples
%exclude %{_docdir}/%{name}/docportal

%files doc
%defattr(-,root,root)
%{_docdir}/%{name}/Examples
%{_docdir}/%{name}/docportal
