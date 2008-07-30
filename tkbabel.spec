Summary:	Tk/Tcl frontend for babelfish language translation
Name:		tkbabel
Version:	0.59
Release:	%mkrel 5
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

