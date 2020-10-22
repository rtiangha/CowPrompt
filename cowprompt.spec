###############################################################################
# Spec file for cowprompt
# Assumes that:
# - 'rpmbuild' directory is in {$HOME} (with proper structure)
# - 'unix' directory from project is in {$HOME} as well (i.e. same level as
#   rpmbuild director)
###############################################################################
Summary: CowPrompt is a wrapper for xcowsay and fortune to display prompts on the screen.
Name: cowprompt
Version: 0.1
Release: 1
License: Unlicense
URL: https://github.com/rtiangha/CowPrompt
Group: Games
Packager: Reg Tiangha
Requires: xcowsay
Requires: (fortune-mod or fortune)
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
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
mkdir -p $RPM_BUILD_ROOT/usr/share/games/fortunes
mkdir -p $RPM_BUILD_ROOT/usr/share/icons
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man6
mkdir -p $RPM_BUILD_ROOT/etc

cp -ar ../../unix/* $RPM_BUILD_ROOT/

exit

%files
%attr(0644, root, root) /etc/*
%attr(0755, root, root) /usr/bin/*
%attr(0644, root, root) /usr/share/*

%clean
rm -rf $RPM_BUILD_ROOT/usr
rm -rf $RPM_BUILD_ROOT/etc


%changelog
* Thu Oct 22 2020 Reg Tiangha <reg@reginaldtiangha.com> 0.1-1
- Initial Release.

# Build with the following syntax from the root GitHub project directory:
# rpmbuild --target noarch -bb ~/rpmbuild/SSPECS/cowprompt.spec

