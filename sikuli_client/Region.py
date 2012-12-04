"""
Classes to fulfill the roles of those described at
    http://doc.sikuli.org/region.html
"""
from . import SikuliClient
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
    @property
    def _contructors(self):
        cls, remote = Region, Region.remote
        assert isinstance(remote, SikuliClient)
        if not hasattr(cls, "__contructors"):
            def _new_xywh(x, y, w, h):
                return remote._eval(
                    "return _new_jython_object(object=Sikuli.Region(x=%r, "
                                                                   "y=%r, "
                                                                   "w=%r, "
                                                                   "h=%r))"%(
                        x, y, w ,h))
            def _new_region(region):
                assert isinstance(region, cls)
                _ = region.remote_id
                return remote._eval(
                    "return self._new_jython_object(object=Sikuli.Region("
                                "self._get_jython_object(%r)"
                            "))" % region.remote_id)
            cls.__contructors = (_new_xywh, _new_region)
        return cls.__contructors
