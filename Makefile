# ============================================================================
#                                 DIRECTIONS
# ============================================================================
#
# To Install:
# 	Install cowprompt:         make install-cowprompt
# 	Install cowprompt-cli:     make install-cowprompt-cli
# 	Install cowprompt-data:    make install-cowprompt-data
# 	Install everything:        make install
#
# To Uninstall:
# 	Uninstall cowprompt:       make uninstall-cowprompt
# 	Uninstall cowprompt-cli:   make uninstall-cowprompt-cli
# 	Uninstall cowprompt-data:  make uninstall-cowprompt-data
# 	Uninstall everything:      make uninstall 
#

# ===========================================================================
#                        CONFIGURATION OPTIONS
# ===========================================================================
#
# APPDIR:      Directory of .desktop app launchers (cowprompt)
# BINDIR:      Directory of executables (cowprompt & cowprompt-cli)
# CONFDIR:     Where the cowprompt configuration file goes (cowprompt)
# FORTUNEDIR:  Directory of fortune data files cowprompt-data)
# ICONDIR:     Root directory desktop icons (cowprompt)
# MANDIR:      Root directory of man pages cowprompt & cowprompt-cli)
#

APPDIR ?= /usr/share/applications
BINDIR ?= /usr/bin
CONFDIR ?= /etc
FORTUNEDIR ?= /usr/share/games/fortunes
ICONDIR ?= /usr/share/icons
MANDIR ?= /usr/share/man

# ============================================================================
#                        END OF CONFIGURATION OPTIONS
# ============================================================================

# Install cowprompt package
install-cowprompt:
	cp unix/usr/bin/cowprompt $(BINDIR)/
	cp unix/usr/share/applications/cowprompt.desktop $(APPDIR)/
	cp unix/usr/share/icons/cow_small.png $(ICONDIR)/
	cp unix/usr/share/man/man6/cowprompt.6.gz $(MANDIR)/man6/

# Install cowprompt-cli package
install-cowprompt-cli:
	cp unix/usr/bin/cowprompt-cli $(BINDIR)/
	cp unix/usr/share/man/man6/cowprompt-cli.6.gz $(MANDIR)/man6/

# Install cowprompt-data package
install-cowprompt-data:
	cp unix/usr/share/games/fortunes/* $(FORTUNEDIR)/

# Install everything
install: install-cowprompt install-cowprompt-cli install-cowprompt-data

# Uninstall cowprompt package
uninstall-cowprompt:
	$(RM) $(BINDIR)/cowprompt
	$(RM) $(APPDIR)/cowprompt.desktop
	$(RM) $(ICONDIR)/cow_small.png 
	$(RM) $(MANDIR)/man6/cowprompt.6.gz

# Uninstall cowprompt-cli package
uninstall-cowprompt-cli:
	$(RM) $(BINDIR)/cowprompt-cli
	$(RM) $(MANDIR)/man6/cowprompt-cli.6.gz

# Uninstall cowprompt-data package
uninstall-cowprompt-data:
	$(RM) $(FORTUNEDIR)/Acute
	$(RM) $(FORTUNEDIR)/Acute.dat
	$(RM) $(FORTUNEDIR)/Complete
	$(RM) $(FORTUNEDIR)/Complete.dat
	$(RM) $(FORTUNEDIR)/Diary
	$(RM) $(FORTUNEDIR)/Diary.dat
	$(RM) $(FORTUNEDIR)/Oblique
	$(RM) $(FORTUNEDIR)/Oblique.dat
	$(RM) $(FORTUNEDIR)/Oblique-ed1
	$(RM) $(FORTUNEDIR)/Oblique-ed1.dat
	$(RM) $(FORTUNEDIR)/Oblique-ed2
	$(RM) $(FORTUNEDIR)/Oblique-ed2.dat
	$(RM) $(FORTUNEDIR)/Oblique-ed3
	$(RM) $(FORTUNEDIR)/Oblique-ed3.dat
	$(RM) $(FORTUNEDIR)/Oblique-ed4
	$(RM) $(FORTUNEDIR)/Oblique-ed4.dat
	$(RM) $(FORTUNEDIR)/Signal
	$(RM) $(FORTUNEDIR)/Signal.dat

# Uninstall everything
uninstall: uninstall-cowprompt uninstall-cowprompt-cli uninstall-cowprompt-data



