Running :mod:`SikuliServer.SikuliServer` on your System Under Test
==================================================================

Getting Started
---------------

For the most part it should be as simple as downloading the repo to your system
under test and running the appropriate script for your operating system --
sikuliserver.bat for windows and sikuliserver.sh for any others. This assumes
that you already have Java 6 and Sikuli X installed on your machine, and that
the paths are correct.

If you want more control of what's going on, you can do::

  from SikuliServer.sikuli_server import SikuliRobotRemoteServer as Server
  Server(port=5637)

where you can change the port if you need to. For more advanced usage please
read the source -- you will see that it is a very simple wrapper around
:mod:`SikuliServer.SikuliServer` using the bundled
:mod:`SikuliServer.sikuli_server.robotremoteserver.RobotRemoteServer`, which is
a static copy taken from
http://robotframework.googlecode.com/hg/tools/remoteserver/robotremoteserver.py


Troubleshooting
---------------

For each of these where I advise to edit the launcher script - it is better to
work on a copy of the launcher script placed in you path with a higher
precidence than the python scripts directory, so that changes are not lost if
you upgrade SikuliServer.

Can't find Java/Libraries
^^^^^^^^^^^^^^^^^^^^^^^^^

First you'll want to check that you have a jvm on your machine - in a terminal
run `java -version`, and check that you get some output. If you don't, you'll
need to install java - how you go about this is specific to your operating
system - try http://java.com/en/download/help/index_installing.xml for help.

If it's still not working, and you're running under a non-windows os, I'm afraid
I don't know what could have gone wrong - I'd advise searching, and if that
doesn't provide results, posting a question on http://serverfault.com/
Please also raise an issue, or submit a patch to this documentation so that the
solution is documented for others.

Under Windows you may find that the path to Java or the libraries is wrong --
under a 32-bit operating system all references to `Program Files (x86)` should
be replaced by references to `Program Files`, or if java is installed elsewhere,
you will need to change the path to point to wherever it is installed.

Can't find Sikuli X
^^^^^^^^^^^^^^^^^^^

Much of this will be the same as the section above- it is important to make sure
that Sikuli X is installed as shown at http://www.sikuli.org/download.html --
then make sure that the paths in the launcher script are accurate to your
install location.

Can't find the scripts
^^^^^^^^^^^^^^^^^^^^^^

Open a python REPL and run the following::

  import SikuliServer
  from os.path import dirname
  print dirname(SikuliServer.__file__)

This should show you the directory within which the launcher scripts reside, if
they have not been copied to anywhere in your path (type sikuliserver.bat or
sikuliserver.sh in your teminal and hit enter) then place a link or copy to the
relavent script in your path.
