#sikuliserver.py
##Aka robotframework-sikuliserver
Jython script to run a robot remote library exposing the Sikuli API (and popen).
You will need Sikuli and java to already be installed.

##Under windows

Should be as simple as running sikuliserver.bat, although some variables may need changing for your installed environment

##Under OSX/Linux/Unix

Under OSX you should be able to just run sikuliserver.sh. Under other operating systems you will need to edit sikuliserver.sh to give the path where you unzipped Sikuli-IDE

##Using with Robotframework

You can choose to either use SikuliServer using Robotframework's remotelibrary, or use SikuliClient to get a more selective interface.

#SiculiClient

This client library is designed to be imported into robotframework to expose keywords directly, or be used from python, in which case there are exposed classes for dealing with more advanced functionality. (not fully defined yet)
