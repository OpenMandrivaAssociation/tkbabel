Summary:	Tk/Tcl frontend for babelfish language translation
Name:		tkbabel
Version:	0.59
Release:	8
License:	GPL
Group:		Communications

Source:		http://members.home.net/sdanis/%{name}/%{name}-%{version}.tar.bz2

URL:		http://members.home.ner/sdanis/%{name}/
Buildarch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Tkbabel and tclbabel are simple Tcl/Tk programs to access babelfish from
either the command line (tclbabel) or from a simple GUI (tkbabel).


%prep
 
%setup -q -n %{name}-%{version}
  
%build
# replace the location of Babelfish.tcl in tkbabel and tclbabel
mv tclbabel tclbabel.orig
#sed -e "s/\/usr\/local\/lib\/tclbabel/\/usr\/share/" tclbabel.orig > tclbabel
perl -pi -e "s,/usr/local/lib/tclbabel/,/usr/share/," tclbabel.orig
perl -pi -e "s,/usr/lib/tclbabel/,/usr/share/," tclbabel.orig
cat tclbabel.orig > tclbabel

mv tkbabel  tkbabel.orig
#sed -e "s/\/usr\/local\/lib\/tclbabel/\/usr\/share/" tkbabel.orig  > tkbabel
perl -pi -e "s,/usr/local/lib/tclbabel/,/usr/share/," tkbabel.orig
perl -pi -e "s,/usr/lib/tclbabel/,/usr/share/," tkbabel.orig
cat tkbabel.orig > tkbabel

%install
rm -fr %buildroot

# install the actual executable
install -m 755 -d $RPM_BUILD_ROOT/usr
install -m 755 -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 -d $RPM_BUILD_ROOT/usr/share
install -m 755 Babelfish.tcl  $RPM_BUILD_ROOT/usr/share/Babelfish.tcl
install -m 755 {tk,tcl}babel  $RPM_BUILD_ROOT%{_bindir}/


%clean
rm -fr %buildroot


%files
%defattr (-,root,root)
%doc CHANGELOG INSTALL LICENSE README USAGE BUGS
%{_bindir}/tclbabel
%{_bindir}/tkbabel
/usr/share/Babelfish.tcl 



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.59-7mdv2010.0
+ Revision: 434401
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.59-6mdv2009.0
+ Revision: 261565
- rebuild
- rebuild

* Wed Jan 09 2008 Nicolas Lécureuil <neoclust@mandriva.org> 0.59-3mdv2008.1
+ Revision: 147259
- Use %%mkrel
- import tkbabel


* Fri Mar 22 2002 David BAUDENS <baudens@mandrakesoft.com> 0.59-2mdk
- Clean after build

* Mon Feb 19 2001 Gregory Letoquart <gletoquart@mandrakesoft.com> 0.59-1mdk
- New version 0.59
- Change source Babelfish.tcl directory
- Add Doc
- Repackaged

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.56-4mdk
- remove packager tag

* Thu Jul 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.56-3mdk
- use tmppath

* Thu Jul 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.56-2mdk
- BM
- use new macros

* Wed Jun 21 2000 Enzo Maggi <enzo@mandrakesoft.com> 0.56-1mdk
- packaged version 0.56

* Tue Mar 28 2000 Enzo Maggi <enzo@mandrakesoft.com> 0.5-3mdk
- repackaged

* Fri Nov 19 1999 Lenny Cartier <lenny@mandrakesoft.com>
- New in contribs
- Specfiles adaptations
- Used the contrib provided by rufus.t.firefly

* Wed Oct 27 1999 rufus t firefly <rufus.t.firefly@linux-mandrake.com>
  [tkbabel-0.5-2mdk]
  - fixed symbolic linking problem
  - moved Babelfish.tcl library to /usr/share, with sed patch
* Wed Oct 12 1999 rufus t firefly <rufus.t.firefly@linux-mandrake.com>
  [tkbabel-0.5-1mdk]
  - converted history to changelog tag
  - updated package to new version 0.5 from freshmeat
* Tue Oct 12 1999 rufus t firefly <rufus.t.firefly@linux-mandrake.com>
  [tkbabel-0.3-1mdk]
  - initial packaging
