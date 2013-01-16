"""
Classes to fulfill the roles of those described at
    http://doc.sikuli.org/region.html
"""
__author__ = 'Alistair Broomhead'
from .sikuli_class import (UnimplementedSikuliClass,
                           SikuliClass,
                           run_on_remote,
                           constructor)
from .location import Location
from .screen import Screen

from .match import Match
from .pattern import Pattern


class SikuliEvent(UnimplementedSikuliClass):
    """ Manages interaction with Sikuli's SikuliEvent """
    #TODO: Settings class
    # http://doc.sikuli.org/region.html#SikuliEvent
    pass


class Region(SikuliClass):
    """ Manages interaction with Sikuli's Region """
    # http://doc.sikuli.org/region.html#Region
    @run_on_remote
    def setX(self, num):
        """
        :param num: number - the new value

        Set the respective attribute of the region to the new value. This
        effectively moves the region around and/or changes its dimension.
        """
        pass

    @run_on_remote
    def setY(self, num):
        """
        :param num: number - the new value

        Set the respective attribute of the region to the new value. This
        effectively moves the region around and/or changes its dimension.
        """
        pass

    @run_on_remote
    def setW(self, num):
        """
        :param num: number - the new value

        Set the respective attribute of the region to the new value. This
        effectively moves the region around and/or changes its dimension.
        """
        pass

    @run_on_remote
    def setH(self, num):
        """
        :param num: number - the new value

        Set the respective attribute of the region to the new value. This
        effectively moves the region around and/or changes its dimension.
        """
        pass

    @run_on_remote
    def moveTo(self, location):
        """
        :param location: Location - the new top left corner
        :rtype : Region - the modified region object

        Set the position of this region regarding its top left corner to the
        given location (the x and y values are modified).
        """
        pass

    @run_on_remote
    def setROI(self, x, y, w, h):
        """
        :param x: number
        :param y: number
        :param w: number
        :param h: number

        Set position and dimension to new values. The motivation for this alias
        is to make scripts more readable: setROI() is intended to restrict the
        search to a smaller area to speed up processing searches (region of
        interest).
        """
        pass

    @run_on_remote
    def setRect(self, x, y, w, h):
        """
        :param x: number
        :param y: number
        :param w: number
        :param h: number

        Set position and dimension to new values. The motivation for this alias
        is to make scripts more readable: setRect() should be used to redefine a
        region (which could be enlarging it).
        """
        pass

    @run_on_remote
    def morphTo(self, region):
        """
        :param region: Region

        Set the position and dimension of this region to the
        corresponding values of the region given as parameter.
        """
        pass

    @run_on_remote
    def getX(self):
        """
        :rtype : int

        Get the respective attribute of the region.
        """
        pass

    @run_on_remote
    def getY(self):
        """
        :rtype : int

        Get the respective attribute of the region.
        """
        pass

    @run_on_remote
    def getW(self):
        """
        :rtype : int

        Get the respective attribute of the region.
        """
        pass

    @run_on_remote
    def getH(self):
        """
        :rtype : int

        Get the respective attribute of the region.
        """
        pass

    @run_on_remote
    def getCenter(self):
        """
        :rtype : Location

        Get the center of the region.
        """
        pass

    @getCenter.func
    def getCenter(self):
        """ :rtype : Location """
        location_id = self.remote._eval(
            "self._new_jython_object("
            "   self._get_jython_object(%r).getCenter())" % self._id)
        return Location(remote=self.remote, server_id=location_id)

    @run_on_remote
    def getTopLeft(self):
        """
        :rtype : Location

        Get the location of the region's respective corner.
        """
        pass

    @getTopLeft.func
    def getTopLeft(self):
        """ :rtype : Location """
        location_id = self.remote._eval(
            "self._new_jython_object("
            "   self._get_jython_object(%r).getTopLeft())" % self._id)
        return Location(remote=self.remote, server_id=location_id)

    @run_on_remote
    def getTopRight(self):
        """
        :rtype : Location

        Get the location of the region's respective corner.
        """
        pass

    @getTopRight.func
    def getTopRight(self):
        """ :rtype : Location """
        location_id = self.remote._eval(
            "self._new_jython_object("
            "   self._get_jython_object(%r).getTopRight())" % self._id)
        return Location(remote=self.remote, server_id=location_id)

    @run_on_remote
    def getBottomLeft(self):
        """
        :rtype : Location

        Get the location of the region's respective corner.
        """
        pass

    @getBottomLeft.func
    def getBottomLeft(self):
        """ :rtype : Location """
        location_id = self.remote._eval(
            "self._new_jython_object("
            "   self._get_jython_object(%r).getBottomLeft())" % self._id)
        return Location(remote=self.remote, server_id=location_id)

    @run_on_remote
    def getBottomRight(self):
        """
        :rtype : Location

        Get the location of the region's respective corner.
        """
        pass

    @getBottomRight.func
    def getBottomRight(self):
        """ :rtype : Location """
        location_id = self.remote._eval(
            "self._new_jython_object("
            "   self._get_jython_object(%r).getBottomRight())" % self._id)
        return Location(remote=self.remote, server_id=location_id)

    @run_on_remote
    def getScreen(self):
        pass

    @getScreen.func
    def getScreen(self):
        location_id = self.remote._eval(
            "self._new_jython_object("
            "   self._get_jython_object(%r).getScreen())" % self._id)
        return Screen(remote=self.remote, server_id=location_id)

    @run_on_remote
    def getLastMatch(self):
        pass

    @getLastMatch.func
    def getLastMatch(self):
        location_id = self.remote._eval(
            "self._new_jython_object("
            "   self._get_jython_object(%r).getLastMatch())" % self._id)
        return Match(remote=self.remote, server_id=location_id)

    @run_on_remote
    def getLastMatches(self):
        pass

    @getLastMatches.func
    def getLastMatches(self):
        location_ids = self.remote._eval(
            "self._new_jython_object("
            "   self._get_jython_object(%r).getLastMatches())" % self._id)
        return (Match(remote=self.remote, server_id=location_id) for
            location_id in location_ids)

    @run_on_remote
    def setAutoWaitTimeout(self, seconds):
        pass

    @run_on_remote
    def getAutoWaitTimeout(self):
        pass

    #20%
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

    #30%
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

    #40%
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

    #50%
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

    #60%
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

    #70%
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

    #80%
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

    #90%
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
