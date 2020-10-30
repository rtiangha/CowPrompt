###############################################################################
# Spec file for cowprompt
# Assumes that:
# - 'rpmbuild' directory is in {$HOME} (with proper structure; i.e. BUILD, ,
#    BUILDROOT, RPMS, SOURCES, SPECS, SRPMS))
# - 'unix' directory from project is symlinked into rpmbuild/SOURCES 
#    i.e
#        ln -s CowPrompt/unix ~/rpmbuild/SOURCES/unix
###############################################################################
Summary: CowPrompt is a wrapper for xcowsay and fortune to display prompts on the screen.
Name: cowprompt
Version: 1.0.1
Release: 1
License: Unlicense
URL: https://github.com/rtiangha/CowPrompt
Group: Games
Packager: Reg Tiangha
Requires: xcowsay
Requires: (fortune-mod or fortune)
Requires: cowprompt-data
BuildRoot: rpmbuild

%description
CowPrompt is a simple wrapper program for xcowsay and fortune that can be used to display any message contained in a fortune data file to the screen.

%prep
################################################################################
# Create the build tree and copy the files from the development directories    #
# into the build tree.                                                         #
################################################################################
echo "BUILDROOT = $RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
mkdir -p $RPM_BUILD_ROOT/usr/share/icons
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man6
mkdir -p $RPM_BUILD_ROOT/etc

cp -a ../SOURCES/unix/etc/cowprompt.config $RPM_BUILD_ROOT/etc/
cp -a ../SOURCES/unix/usr/bin/cowprompt $RPM_BUILD_ROOT/usr/bin/
cp -a ../SOURCES/unix/usr/share/man/man6/cowprompt.6.gz $RPM_BUILD_ROOT/usr/share/man/man6/
cp -a ../SOURCES/unix/usr/share/icons/cow_small.png $RPM_BUILD_ROOT/usr/share/icons/
cp -a ../SOURCES/unix/usr/share/applications/cowprompt.desktop $RPM_BUILD_ROOT/usr/share/applications/

exit

%files
%attr(0644, root, root) /etc/*
%attr(0755, root, root) /usr/bin/*
%attr(0644, root, root) /usr/share/*

%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Fri Oct 30 2020 Reg Tiangha <reg@reginaldtiangha.com> 1.0.1-1
- Minor updates to documentation.

* Thu Oct 29 2020 Reg Tiangha <reg@reginaldtiangha.com> 1.0-1
- Separate out fortune data files to a separate package.
- Now requires the additional installation of the cowprompt-data pacakge.

* Fri Oct 23 2020 Reg Tiangha <reg@reginaldtiangha.com> 0.2-1
- Switch to using variable names rather than hard coded values
- Add additional data files based on other strategies (see http://www.rtqe.net/ObliqueStrategies/EditionOther.html )

* Thu Oct 22 2020 Reg Tiangha <reg@reginaldtiangha.com> 0.1-1
- Initial Release.

# Build with the following syntax from the root of the CowPrompt project directory:
# rpmbuild --target noarch -bb cowprompt.spec

