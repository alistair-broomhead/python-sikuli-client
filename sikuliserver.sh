#!/bin/sh

#
# This is the path to the sikuli-script jar as found on osx, update to reflect
# your platform
#
PATH_TO_SIKULI_JAR=/Applications/Sikuli-IDE.app/Contents/Resources/Java/
java -cp "$PATH_TO_SIKULI_JAR/sikuli-script.jar" org.python.util.jython sikuliserver.py
