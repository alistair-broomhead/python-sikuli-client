SET OLDPATH=%PATH%
::
:: These paths are the defaults for Sikuli X and Java 7 - if they're not
:: correct, change them
::
SET PATH=%OLDPATH%;C:\Program Files (x86)\Sikuli X\libs
SET PATH=%OLDPATH%;C:\Program Files (x86)\Java\jre7\lib
::
::  This should already be set, but if not, uncomment it
::
::  SET SIKULI_HOME=C:\Program Files (x86)\Sikuli X\
java -cp "%SIKULI_HOME%sikuli-script.jar" org.python.util.jython sikuliserver.py
SET PATH=%OLDPATH%
