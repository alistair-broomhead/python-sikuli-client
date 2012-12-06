"""
Classes to fulfill the roles of those described at
    http://doc.sikuli.org/region.html
"""
__author__ = 'Alistair Broomhead'
from .sikuli_class import (UnimplementedSikuliClass,
                           SikuliClass,
                           run_on_remote,
                           constructor)

class SikuliEvent(UnimplementedSikuliClass):
    """ Manages interaction with Sikuli's SikuliEvent """
    #TODO: Settings class
    # http://doc.sikuli.org/region.html#SikuliEvent
    pass


#noinspection PyDocstring
class Region(SikuliClass):
    """ Manages interaction with Sikuli's Region """
    # http://doc.sikuli.org/region.html#Region
    @run_on_remote
    def setX(self, num): pass
    @run_on_remote
    def setY(self, num): pass
    @run_on_remote
    def setW(self, num): pass
    @run_on_remote
    def setH(self, num): pass
    @run_on_remote
    def moveTo(self, location): pass
    @moveTo.arg
    def moveTo(self, location):
        return location._str_get,
    @run_on_remote
    def setROI(self, x, y, w, h): pass
    @run_on_remote
    def setRect(self, x, y, w, h): pass
    @run_on_remote
    def morphTo(self, region): pass
    @morphTo.arg
    def morphTo(self, region):
        return region._str_get,
    @run_on_remote
    def getX(self): pass
    @run_on_remote
    def getY(self): pass
    @run_on_remote
    def getW(self): pass
    @run_on_remote
    def getH(self): pass
    @run_on_remote
    def getCenter(self): pass
    @getCenter.func
    def getCenter(self):
        location_id = self.remote._eval(
            "self._new_jython_object("
            "   self._get_jython_object(%r).getCenter())" %self._id)
        from .location import Location
        return Location(remote=self.remote, server_id=location_id)

    #progress marker
    @run_on_remote
    def getTopLeft(self): pass
    @run_on_remote
    def getTopRight(self): pass
    @run_on_remote
    def getBottomLeft(self): pass
    @run_on_remote
    def getBottomRight(self): pass
    @run_on_remote
    def getScreen(self): pass
    @run_on_remote
    def getLastMatch(self): pass
    @run_on_remote
    def getLastMatches(self): pass
    @run_on_remote
    def setAutoWaitTimeout(self, seconds): pass
    @run_on_remote
    def getAutoWaitTimeout(self): pass
    @run_on_remote
    def offset(self): pass
    @run_on_remote
    def inside(self): pass
    @run_on_remote
    def nearby(self): pass
    @run_on_remote
    def above(self): pass
    @run_on_remote
    def below(self): pass
    @run_on_remote
    def left(self): pass
    @run_on_remote
    def right(self): pass
    @run_on_remote
    def find(self): pass
    @run_on_remote
    def findAll(self): pass
    @run_on_remote
    def wait(self): pass
    @run_on_remote
    def waitVanish(self): pass
    @run_on_remote
    def exists(self): pass
    @run_on_remote
    def onAppear(self): pass
    @run_on_remote
    def onVanish(self): pass
    @run_on_remote
    def onChange(self): pass
    @run_on_remote
    def observe(self): pass
    @run_on_remote
    def stopObserver(self): pass
    @run_on_remote
    def click(self): pass
    @run_on_remote
    def doubleClick(self): pass
    @run_on_remote
    def rightClick(self): pass
    @run_on_remote
    def highlight(self): pass
    @run_on_remote
    def hover(self): pass
    @run_on_remote
    def dragDrop(self): pass
    @run_on_remote
    def drag(self): pass
    @run_on_remote
    def dropAt(self): pass
    @run_on_remote
    def type(self): pass
    @run_on_remote
    def paste(self): pass
    @run_on_remote
    def text(self): pass
    @run_on_remote
    def mouseDown(self): pass
    @run_on_remote
    def mouseUp(self): pass
    @run_on_remote
    def mouseMove(self): pass
    @run_on_remote
    def wheel(self): pass
    @run_on_remote
    def keyDown(self): pass
    @run_on_remote
    def keyUp(self): pass
    @run_on_remote
    def setFindFailedResponse(self): pass
    @run_on_remote
    def getFindFailedResponse(self): pass
    @run_on_remote
    def setThrowException(self): pass
    @run_on_remote
    def getThrowException(self): pass
    @run_on_remote
    def getRegionFromPSRM(self): pass
    @run_on_remote
    def getLocationFromPSRML(self): pass
@constructor(Region)
def _region_constructor(x, y, w, h):
    return "Sikuli.Region(%r, %r, %r, %r)" % (x, y, w, h)
@constructor(Region)
def _region_constructor(region):
    return "Sikuli.Region(%s)" % region._str_get
