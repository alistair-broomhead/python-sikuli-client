"""

:class:`Region` and :class:`SikuliEvent` classes to fulfill the roles of those
described at http://doc.sikuli.org/region.html

.. toctree::
   :maxdepth: 2

"""
__author__ = 'Alistair Broomhead'
from .sikuli_class import (UnimplementedSikuliClass,
                           SikuliClass,
                           run_on_remote,
                           return_from_remote,
                           constructor)
from .misc import assert_positive_int
from .location import Location
from .screen import Screen

from .match import Match
from .pattern import Pattern


class SikuliEvent(UnimplementedSikuliClass):
    """
    Manages interaction with Sikuli's SikuliEvent, reflecting
    http://doc.sikuli.org/region.html#SikuliEvent

    .. todo:: Implement

    """
    #TODO: SikuliEvent class
    pass


class Region(SikuliClass):
    """
    Manages interaction with Sikuli's Region, reflecting
    http://doc.sikuli.org/region.html#Region
    """

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

    @return_from_remote('Region')
    def moveTo(self, location):
        """
        :param location: :class:`~sikuli_client.location.Location` - the new top left corner
        :rtype: :class:`Region` -- the modified region object

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
        :param region: :class:`Region`

        Set the position and dimension of this region to the
        corresponding values of the region given as parameter.
        """
        pass

    @run_on_remote
    def getX(self):
        """
        :rtype: int

        Get the respective attribute of the region.
        """
        pass

    @run_on_remote
    def getY(self):
        """
        :rtype: int

        Get the respective attribute of the region.
        """
        pass

    @run_on_remote
    def getW(self):
        """
        :rtype: int

        Get the respective attribute of the region.
        """
        pass

    @run_on_remote
    def getH(self):
        """
        :rtype: int

        Get the respective attribute of the region.
        """
        pass

    @return_from_remote(Location)
    def getCenter(self):
        """
        :rtype: :class:`~sikuli_client.location.Location`

        Get the center of the region.
        """
        pass

    @return_from_remote(Location)
    def getTopLeft(self):
        """
        :rtype: :class:`~sikuli_client.location.Location`

        Get the location of the region's respective corner.
        """
        pass

    @return_from_remote(Location)
    def getTopRight(self):
        """
        :rtype: :class:`~sikuli_client.location.Location`

        Get the location of the region's respective corner.
        """
        pass

    @return_from_remote(Location)
    def getBottomLeft(self):
        """
        :rtype: :class:`~sikuli_client.location.Location`

        Get the location of the region's respective corner.
        """
        pass

    @return_from_remote(Location)
    def getBottomRight(self):
        """
        :rtype: :class:`~sikuli_client.location.Location`

        Get the location of the region's respective corner.
        """
        pass

    @return_from_remote(Screen)
    def getScreen(self):
        """
        :rtype: :class:`~sikuli_client.screen.Screen`

        Returns the screen object that contains this region.

        This method only makes sense in Multi Monitor Environments, since it
        always returns the default screen in a single monitor environment.
        """
        pass

    @return_from_remote(Match)
    def getLastMatch(self):
        """
        :rtype: :class:`~sikuli_client.match.Match`

        All successful find operations (explicit like find() or implicit like
        click()), store the best match in the lastMatch attribute of the region
        that was searched.
        """
        pass

    @run_on_remote
    def getLastMatches(self):
        """
        :rtype: generator

        findAll() stores all found matches into lastMatches attribute of the
        region that was searched as a generator.
        """
        pass

    @getLastMatches.func
    def getLastMatches(self):
        """ :rtype: generator """
        location_ids = self.remote._eval(
            "[self._new_jython_object(x) for x in"
            " self._get_jython_object(%r).getLastMatches()]" % self._id)
        return (Match(remote=self.remote, server_id=location_id)
                for location_id in location_ids)

    @run_on_remote
    def setAutoWaitTimeout(self, seconds):
        """
        :param seconds: float - The internal granularity is milliseconds.

        Set the maximum waiting time for all subsequent find operations.

        This method enables all find operations to wait for the given pattern to
        appear until the specified amount of time has elapsed. The default is
        3.0 seconds. This method is intended for users to override this default
        setting. As such it lets Region.find() work like Region.wait(), without
        being able to set an individual timeout value for a specific find
        operation.
        """
        pass

    @run_on_remote
    def getAutoWaitTimeout(self):
        """
        :rtype: float

        Get the current value of the maximum waiting time for find operations
        """
        pass

    @return_from_remote('Region')
    def offset(self, location):
        """
        Returns a new Region object, whose upper left corner is relocated adding
        the location's x and y value to the respective values of the given
        region. Width and height are the same. So this clones a region at a
        different place.

        :param location: :class:`~sikuli_client.location.Location`
        :rtype: :class:`Region`

        .. code-block:: python

            new_reg = reg.offset(Location(xoff, yoff)) # same as
            new_reg = Region(reg.x + xoff, reg.y + yoff, reg.w, reg.h)
        """
        pass

    @return_from_remote('Region')
    def inside(self):
        """
        Returns the same object. Retained for upward compatibility.

        This method can be used to make scripts more readable.
        ``region.inside().find()`` is totally equivalent to ``region.find()``.

        :rtype: :class:`Region`
        """
        pass

    @return_from_remote('Region')
    def nearby(self, range_px=50):
        """
        Returns a new Region that includes the nearby neighbourhood of the
        the current region. The new region is defined by extending the
        current region's dimensions in all directions by range number of
        pixels. The center of the new region remains the same.

        :param range_px: int > 0, default = 50
        :rtype: :class:`Region`
        """
        assert_positive_int(range_px,self.nearby)

    @return_from_remote('Region')
    def above(self, range_px):
        """
        Returns a new :py:class:`Region` that is defined above the current
        region's
        top border with a height of *range* number of pixels.
        So it does not include the current    region.
        If *range* is omitted, it reaches to the top
        of the screen. The new region has the same width and x-position as the
        current region.

        :param range_px: a positive integer defining the new height
        :return: a :class:`Region` object
        """
        assert_positive_int(range_px, self.above)

    @return_from_remote('Region')
    def below(self, range_px):
        """
        Returns a new :py:class:`Region` that is defined below the current
        region's
        bottom border with a height of *range* number of pixels.
        So it does not include the current    region.
        If *range* is omitted, it reaches to the bottom
        of the screen. The new region has the same width and x-position as the
        current region.

        :param range_px: a positive integer defining the new height
        :return: a :class:`Region` object
        """
        assert_positive_int(range_px, self.below)

    @return_from_remote('Region')
    def left(self, range_px):
        """
        Returns a new :py:class:`Region` that is defined left of the current
        region's
        left border with a width of *range* number of pixels.
        So it does not include the current    region.
        If *range* is omitted, it reaches to the left border
        of the screen. The new region has the same height and y-position as the
        current region.

        :param range_px: a positive integer defining the new width
        :return: a :py:class:`Region` object
        """
        assert_positive_int(range_px, self.left)

    @return_from_remote('Region')
    def right(self, range_px):
        """
        Returns a new :py:class:`Region` that is defined right of the current
        region's right border with a width of *range* number of pixels.
        So it does not include the current  region.
        If *range* is omitted, it reaches to the right border
        of the screen. The new region has the same height and y-position as the
        current region.

        :param range_px: a positive integer defining the new width
        :return: a :py:class:`Region` object
        """
        assert_positive_int(range_px, self.right)

    @run_on_remote
    def find(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def findAll(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def wait(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    #40%
    @run_on_remote
    def waitVanish(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def exists(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def onAppear(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def onVanish(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def onChange(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    #50%
    @run_on_remote
    def observe(self):
        """
        .. todo:: Implement
        """
        pass

    @run_on_remote
    def stopObserver(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def click(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def doubleClick(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def rightClick(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    #60%
    @run_on_remote
    def highlight(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def hover(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def dragDrop(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def drag(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def dropAt(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    #70%
    @run_on_remote
    def type(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def paste(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def text(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def mouseDown(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def mouseUp(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    #80%
    @run_on_remote
    def mouseMove(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def wheel(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def keyDown(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def keyUp(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def setFindFailedResponse(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    #90%
    @run_on_remote
    def getFindFailedResponse(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def setThrowException(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def getThrowException(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def getRegionFromPSRM(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @run_on_remote
    def getLocationFromPSRML(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass


@constructor(Region)
def _region_constructor(x, y, w, h):
    return "Sikuli.Region(%r, %r, %r, %r)" % (x, y, w, h)


@constructor(Region)
def _region_constructor(region):
    return "Sikuli.Region(%s)" % region._str_get
