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
    setX = lambda self, num: self.remote._eval(
        "self._get_jython_object(%r).setX(%r)" % (self.server_id, num))
    setY = lambda self, num: self.remote._eval(
        "self._get_jython_object(%r).setY(%r)" % (self.server_id, num))
    setW = lambda self, num: self.remote._eval(
        "self._get_jython_object(%r).setW(%r)" % (self.server_id, num))
    setH = lambda self, num: self.remote._eval(
        "self._get_jython_object(%r).setH(%r)" % (self.server_id, num))
    getX = lambda self: self.remote._eval(
        "self._get_jython_object(%r).getX()" % self.server_id)
    getY = lambda self: self.remote._eval(
        "self._get_jython_object(%r).getY()" % self.server_id)
    getW = lambda self: self.remote._eval(
        "self._get_jython_object(%r).getW()" % self.server_id)
    getH = lambda self: self.remote._eval(
        "self._get_jython_object(%r).getH()" % self.server_id)
