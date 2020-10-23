# CowPrompt
**CowPrompt** is a simple wrapper script for `xcowsay` and `fortune` that can be used to display any message contained in a single, specific fortune data file to the screen.

## What is it for?
The main intent for CowPrompt is to display writing or creative prompts for writers taking part in self-challenges such as [NaNoWriMo](https://nanowrimo.org), but can also be used for any purpose where prompts or messages need to be displayed onto the screen on demand.

## Why does CowPrompt need to exist? Why not just use `xcowfortune` which is also installed with `xcowsay`, or use `xcowsay's` existing functionality?
You could do that, but it would also pull from every fortune data file installed on the system by default, rather than just one (which may or may not be what you want). You could also pipe the output of fortune (or a specific fortune data file) through `xcowsay` on the command line.

However, I wanted a simple way to be able to:

1. Configure the command to use only one fortune data file rather than all of them in *specific* cases (in this case, a fortune data file that specifically contained various creative prompts to try and help me get through writer's block), and more importantly,
2. Be able to invoke the command through a launcher on the desktop, application menu, or quick launch panel rather than through the command line, hence the desire for a wrapper script.

I'd essentially have to write my own script to do the above (the alternative being to modify xcowfortune to take an additional argument to specify a specific fortune data file), so I made one for myself and decided to share it. It needed a fancy name, and thus, `cowprompt` was born.

## How it Works
By default, CowPrompt displays quotes from a combined set of **Brian Eno's** [Oblique Strategies](https://en.wikipedia.org/wiki/Oblique_Strategies) cards (specifically, Editions 1-4 with duplicates removed, which is [available for viewing online](http://www.rtqe.net/ObliqueStrategies/Edition1-3.html)) in fortune data file format, but CowPrompt can be configured to use any specific fortune data file.

Various display options including display position and image file can be configured through editing the `cowprompt.conf` file and the `cowprompt` wrapper executable script.

## Dependencies
CowPrompt can work on any Linux or Unix based system running an X Windows environment that has [xcowsay](https://github.com/nickg/xcowsay) and [fortune](https://en.wikipedia.org/wiki/Fortune_(Unix)) (or [fortune-mod](https://github.com/shlomif/fortune-mod)) available and installed on the system.

## How to Install
CowPrompt can be installed via binary package (.deb and .rpm provided via the [Releases](https://github.com/rtiangha/CowPrompt/Releases) section), or by copying the various files to their respective places onto the file system.

1. First, ensure that the software requirements (`xcowsay` and `fortune`) are installed first. Some examples on how to do so on various distributions are provided below.

### Debian/Ubuntu
`sudo apt-get install xcowsay fortune-mod`

### Fedora/RHEL/CentOS
`sudo dnf install xcowsay fortune-mod`

### openSUSE
`sudo zypper install xcowsay fortune`

2. Next, install the **CowPrompt** package.

### DEB-based Distributions (ex. Debian/Ubuntu, etc.)
`sudo dpkg -i cowprompt_0.1-1_all.deb`

If it complains that you're missing dependencies because you forgot to install `xcowsay` and `fortune-mod`first, simply run:

`sudo apt-get install -f`

and it will automatically fetch any missing dependencies.

### RPM-based Distributions (ex. Fedora/RHEL/CentOS/openSUSE, etc.)
`sudo rpm -ivh cowprompt-0.1-1.noarch.rpm`

### Other Distributions
Ensure that `xcowsay` and `fortune` are installed in your system (either through your distribution's package manager or by manually compiling it) and then copy the files in the `unix` directory of the CowPrompt project page to their equivalent places in your distribution's file system.

## How to Configure
Options to change how/what CowPrompt displays are available via editing the `/etc/cowprompt.conf` file and/or the `/usr/bin/cowprompt` wrapper script. Instructions and examples are included within the files.

## How to Use
To display a random prompt, simply click on the CowPrompt application launcher in your window manager's application menu. You can also invoke it on the command line by typing `cowprompt` in a terminal. To make access easier, you may want to consider adding shortcuts to your Desktop or Quick Launch panel.

## How to Create New Prompts
CowPrompt can pull from any message contained in a valid fortune data file installed on the system. There are many sources to get fortune data files. Your operating system distribution may have additional ones that you can install outside of the default set, or you can find many on the internet that other people have made as well.

Creating your own is easy too. For example, [here is a tutorial](http://bradthemad.org/tech/notes/fortune_makefile.php).

Once you've obtained or created your own custom fortune text and `.dat` files, make sure to copy them to where the other fortune data files live on your system (usually in `/usr/share/games/fortunes` but your distribution may vary) and then edit the `/usr/bin/cowprompt` wrapper script to use it instead of the default `Oblique` file (for example, replace `Oblique` with `Oblique-ed3` to specifically pull from Oblique Strategies, 3rd Edition).

## CREDITS
Special thanks to Nick Gasson for creating [xcowsay](http://www.doof.me.uk/xcowsay) as a super-simple way to output text to a screen in a graphical way, and to [The Oblique Strategies](http://www.rtqe.net/ObliqueStrategies/) website for making the text of Editions 1-4 available for [online viewing](http://www.rtqe.net/ObliqueStrategies/Edition1-3.html) .

## LICENSE

```
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/> 
```

