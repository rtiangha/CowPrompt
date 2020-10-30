###############################################################################
# Spec file for cowprompt-data
# Assumes that:
# - 'rpmbuild' directory is in {$HOME} (with proper structure; i.e. BUILD, ,
#    BUILDROOT, RPMS, SOURCES, SPECS, SRPMS))
# - 'unix' directory from project is symlinked into rpmbuild/SOURCES 
#    i.e
#        ln -s CowPrompt/unix ~/rpmbuild/SOURCES/unix
###############################################################################
Summary: cowprompt-data contains the data files used for CowPrompt, a wrapper for xcowsay and fortune to display prompts on the screen.
Name: cowprompt-data
Version: 1.0 
Release: 1
License: Unlicense
URL: https://github.com/rtiangha/CowPrompt
Group: Games
Packager: Reg Tiangha
Requires: (fortune-mod or fortune)
BuildRoot: rpmbuild

%description
cowprompt-data contains the data files used for CowPrompt, a simple wrapper program for xcowsay (or cowsay) and fortune that can be used to display any message contained in a fortune data file to the screen. Can also be used alone with fortune.

%prep
################################################################################
# Create the build tree and copy the files from the development directories    #
# into the build tree.                                                         #
################################################################################
echo "BUILDROOT = $RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/usr/share/games/fortunes

cp -a ../SOURCES/unix/usr/share/games/fortunes/* $RPM_BUILD_ROOT/usr/share/games/fortunes/

exit

%files
%attr(0644, root, root) /usr/share/*

%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Thu Oct 29 2020 Reg Tiangha <reg@reginaldtiangha.com> 1.0-1
- Initial Release.

# Build with the following syntax from the root of the CowPrompt project directory:
# rpmbuild --target noarch -bb cowprompt-data.spec

