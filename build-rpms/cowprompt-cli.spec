###############################################################################
# Spec file for cowprompt-cli
# Assumes that:
# - 'rpmbuild' directory is in {$HOME} (with proper structure; i.e. BUILD, ,
#    BUILDROOT, RPMS, SOURCES, SPECS, SRPMS))
# - 'unix' directory from project is symlinked into rpmbuild/SOURCES 
#    i.e
#        ln -s CowPrompt/unix ~/rpmbuild/SOURCES/unix
###############################################################################
Summary: cowprompt-cli is a wrapper for xcowsay and fortune to display prompts on a terminal screen.
Name: cowprompt-cli
Version: 1.0 
Release: 1
License: Unlicense
URL: https://github.com/rtiangha/CowPrompt
Group: Games
Packager: Reg Tiangha
Requires: cowsay
Requires: (fortune-mod or fortune)
Requires: cowprompt-data
BuildRoot: rpmbuild

%description
cowprint-cli is a simple wrapper program for xcowsay and fortune that can be used to display any message contained in a fortune data file to the screen.

%prep
################################################################################
# Create the build tree and copy the files from the development directories    #
# into the build tree.                                                         #
################################################################################
echo "BUILDROOT = $RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man6

cp -a ../SOURCES/unix/usr/bin/cowprompt-cli $RPM_BUILD_ROOT/usr/bin/
cp -a ../SOURCES/unix/usr/share/man/man6/cowprompt-cli.6.gz $RPM_BUILD_ROOT/usr/share/man/man6/

exit

%files
%attr(0755, root, root) /usr/bin/*
%attr(0644, root, root) /usr/share/*

%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Thu Oct 29 2020 Reg Tiangha <reg@reginaldtiangha.com> 1.0-1
- Initial Release.

# Build with the following syntax from the root of the CowPrompt project directory:
# rpmbuild --target noarch -bb cowprompt-cli.spec

