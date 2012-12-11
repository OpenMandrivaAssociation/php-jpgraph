%undefine __find_provides
%undefine __find_requires

%define rel	2
%define prerel	b1

Summary:	An OO graph drawing class library for PHP5
Name:		php-jpgraph
Version:	3.5.0
Release:	%mkrel -c %{prerel} %{rel}
License:	QPL
Group:		Networking/Other
URL:		http://jpgraph.net/
# no direct download link available on website
# md5 checksum: 7237ef5dc19ad8bb67197a19782e950c
Source0:	jpgraph-%{version}%{prerel}.tar.gz
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
%setup -q -n jpgraph-%{version}%{prerel}
%patch0 -p0

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/php/jpgraph
cp -aRf src/* %{buildroot}%{_datadir}/php/jpgraph/

install -d -m 755 %{buildroot}%{_docdir}/%{name}
cp -r docs %{buildroot}%{_docdir}/%{name}
cp -r src/Examples %{buildroot}%{_docdir}/%{name}
install -m 644 README VERSION %{buildroot}%{_docdir}/%{name}

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


%changelog
* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 3.5.0-0.b1.2mdv2011.0
+ Revision: 679258
- mass rebuild

* Mon Oct 25 2010 Jani Välimaa <wally@mandriva.org> 3.5.0-0.b1.1mdv2011.0
+ Revision: 589371
- new version 3.5.0b1

* Tue Jul 13 2010 Jani Välimaa <wally@mandriva.org> 3.0.7-1mdv2011.0
+ Revision: 552136
- new version 3.0.7
- fix URLs
- fix some typos in description and summary

* Sat Dec 26 2009 Oden Eriksson <oeriksson@mandriva.com> 3.0.6-1mdv2010.1
+ Revision: 482455
- 3.0.6
- P0: security fix for CVE-2009-4422

* Thu Oct 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.3-4mdv2010.0
+ Revision: 452370
- fix dependencies
- don't suplicate spec-helper job
- spec cleanup
- install documentation under %%{_docdir}/%%{name}
- install php files under %%{_datadir}/php

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 2.3.3-3mdv2010.0
+ Revision: 397545
- Rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 2.3.3-2mdv2009.1
+ Revision: 321861
- rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 2.3.3-1mdv2009.0
+ Revision: 239139
- 2.3.3

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Mar 08 2007 Emmanuel Andry <eandry@mandriva.org> 2.1.4-1mdv2007.1
+ Revision: 138537
- Import php-jpgraph

