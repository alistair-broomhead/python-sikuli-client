"""
Classes to fulfill the roles of those described at
    http://doc.sikuli.org/region.html
"""
__author__ = 'Alistair Broomhead'
from .sikuli_class import UnimplementedSikuliClass, SikuliClass

class SikuliEvent(UnimplementedSikuliClass):
    """ Manages interaction with Sikuli's SikuliEvent """
    #TODO: Settings class
    # http://doc.sikuli.org/region.html#SikuliEvent
    pass


#noinspection PyDocstring
class Region(SikuliClass):
    """ Manages interaction with Sikuli's Region """
    # http://doc.sikuli.org/region.html#Region
    _constructors = (
        lambda x, y, w, h: (Region.remote._eval(
            "self._new_jython_object(Sikuli.Region%r)"%((x, y, w, h),))),
        lambda region: (Region.remote._eval(
            "self._new_jython_object(Sikuli.Region("
                "self._get_jython_object(%r)))" % region.server_id))
    )
    @SikuliClass.run_on_remote
    def setX(self, num): pass
    @SikuliClass.run_on_remote
    def setY(self, num): pass
    @SikuliClass.run_on_remote
    def setW(self, num): pass
    @SikuliClass.run_on_remote
    def setH(self, num): pass
    @SikuliClass.run_on_remote
    def getX(self): pass
    @SikuliClass.run_on_remote
    def getY(self): pass
    @SikuliClass.run_on_remote
    def getW(self): pass
    @SikuliClass.run_on_remote
    def getH(self): pass
