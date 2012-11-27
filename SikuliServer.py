"""
Jython script to run a robot remote library exposing the Sikuli API (and popen)

Under windows run like so (if installed to "C:\Program Files (x86)\Sikuli X\"):

    SET OLDPATH=%PATH%
    SET PATH=%OLDPATH%;C:\Program Files (x86)\Sikuli X\libs
    SET PATH=%OLDPATH%;C:\Program Files (x86)\Java\jre7\lib
    SET SIKULI_HOME=C:\Program Files (x86)\Sikuli X\
    java -cp "%SIKULI_HOME%sikuli-script.jar" org.python.util.jython sikuliserver.py
    SET PATH=%OLDPATH%

Under bash this works ($PATH_TO_SIKULI is what you set in sikuli_installer):

    OLDPATH=$PATH
    PATH=$OLDPATH:$PATH_TO_SIKULI/lib
    java -cp "$PATH_TO_SIKULI/sikuli-script.jar" org.python.util.jython sikuliserver.py
    PATH=$OLDPATH

"""

class SikuliServer(object):
    """
    Class into which to dump the namespace of sikuli.Sikuli
    """
    def eval_jython(self, jython_as_string):
        """
        Gives a quick and dirty way to run jython directly on the SiculiServer -
        not intended for direct use, but for giving an interface for building a
        remote API
        """
        return eval(jython_as_string)
    def __init__(self):
        #noinspection PyUnresolvedReferences
        from sikuli import Sikuli
        self.__dict__.update(Sikuli.__dict__)


def run():
    """ runs the server """
    from robotremoteserver import RobotRemoteServer
    from socket import gethostname
    RobotRemoteServer(library=SikuliServer(),
                      host=gethostname(),
                      port=5637,
                      allow_stop=True)

if __name__ == "__main__":
    run()
