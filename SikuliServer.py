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
    Class nto which to dump the namespace of sikuli.Sikuli
    """
    def __init__(self):
        from sikuli import Sikuli
        self.__dict__.update(Sikuli.__dict__)

class RemoteLib(object):
    def __init__(self, remote):self.__lib = remote
    def __getattr__(self, name):
            if name in self.__lib.get_keyword_names():
                    def _(*args):return self.__lib.run_keyword(name, args)
                    _.__name__ = name
                    self.__dict__[name] = _
                    return _
            raise AttributeError()

def run():
    from robotremoteserver import RobotRemoteServer
    from socket import gethostname
    RobotRemoteServer(library=SikuliServer(),
                      host=gethostname(),
                      port=5637,
                      allow_stop=True)

if __name__ == "__main__":
    run()