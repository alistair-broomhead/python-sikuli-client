"""

:class:`Region` and :class:`SikuliEvent` classes to fulfill the roles of those
described at http://doc.sikuli.org/region.html

.. toctree::
   :maxdepth: 2

"""
from .asserts import (assert_positive_int,
                      assert_PS,
                      assert_positive_num)
__author__ = 'Alistair Broomhead'
from .sikuli_class import (UnimplementedSikuliClass,
                           SikuliClass,
                           run_on_remote,
                           return_from_remote,
                           constructor,
                           TODO,
                           DEFERRED)
from .location import Location
from .screen import Screen

from .match import Match


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
        :rtype: a :class:`Region` object
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
        :rtype: a :class:`Region` object
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
        :rtype: a :py:class:`Region` object
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
        :rtype: a :py:class:`Region` object
        """
        assert_positive_int(range_px, self.right)

    @return_from_remote(Match)
    def find(self, PS):
        """
        :param PS: a :class:`~sikuli_client.pattern.Pattern` object or a string
            (path to an image file or just plain text)
        :rtype: a :class:`~sikuli_client.match.Match` object that contains the
            best match or fails if PatternNotFound

        Find a particular GUI element, which is seen as the given image or
        just plain text. The given file name of an image specifies the
        element's
        appearance. It searches within the region and returns the best match,
        which shows a similarity greater than the minimum similarity given by
        the pattern. If no similarity was set for the pattern by
        :py:meth:`Pattern.similar` before, a default minimum similarity of 0.7
        is set automatically.

        If autoWaitTimeout is set to a non-zero value, find() just acts as a
        wait().

        **Side Effect** *lastMatch*: the best match can be accessed using
        :py:meth:`Region.getLastMatch` afterwards.
        """
        assert_PS(PS, self.find)

    @run_on_remote
    def findAll(self, PS):
        """
        :param PS: a :class:`~sikuli_client.pattern.Pattern` object or a string
            (path to an image file or just plain text)
        :rtype: one or more :class:`~sikuli_client.match.Match` objects as an
            iterator object or fails if PatternNotFound

        Repeatedly find ALL instances of a pattern, until no match can be
        found anymore, that meets the requirements for a single
        :py:meth:`Region.find()` with the specified pattern.

        By default, the returned matches are sorted by the similiarty.
        If you need them ordered by their positions, say the Y coordinates,
        you have to use Python's `sorted <http://wiki.python
        .org/moin/HowTo/Sorting/>`_ function. Here is a example of sorting the
        matches from top to bottom.

        .. code-block:: python

            def by_y(match):
               return match.y

            icons = findAll("png_icon.png")
            # sort the icons by their y coordinates and put them into a new
            sorted_icons = sorted(icons, key=by_y)
            # another shorter version is using lambda.
            sorted_icons = sorted(icons, key=lambda m:m.y)
            for icon in sorted_icons:
               pass # do whatever you want to do with the sorted icons



        **Side Effect** *lastMatches*: a reference to the returned iterator
        object containing the
        found matches is stored with the region that was searched. It can be
        accessed using getLastMatches() afterwards.
        """
        assert_PS(PS, self.find)
        pass

    @findAll.func
    def findAll(self, PS):
        """
        :rtype: generator
        :param PS: a :class:`~sikuli_client.pattern.Pattern` object or a string
            (path to an image file or just plain text)
        """
        match_ids = self.remote._eval(
            "[self._new_jython_object(x) for x in"
            " self._get_jython_object(%r).findAll(%s)]"
            % (self._id,
               PS._str_get if isinstance(PS, SikuliClass) else PS))
        return (Match(remote=self.remote, server_id=match_id)
                for match_id in match_ids)

    @return_from_remote(Match)
    def wait(self, PS=None, seconds=None):
        """
        :param PS: a :class:`~sikuli_client.pattern.Pattern` object or a string
            (path to an image file or just plain text)
        :param seconds: a number, which can have a fraction, as maximum waiting
            time in seconds. The internal granularity is milliseconds. If not
            specified, the auto wait timeout value set by
            :py:meth:`Region.setAutoWaitTimeout` is used. Use the string
            *'FOREVER'* to wait for an infinite time.
        :rtype: a :class:`~sikuli_client.match.Match` object that contains the
            best match or fails if PatternNotFound

        If *PS* is not specified, the script just pauses for the specified
        amount of time. It is still possible to use ``sleep(seconds)`` instead,
        but this is deprecated.

        If *PS* is specified, it keeps searching the given pattern in the
        region until the image appears ( would have been found with
        :py:meth:`Region.find`) or the specified amount of time has elapsed. At
        least one find operation is performed, even if 0 seconds is
        specified.)

        **Side Effect** *lastMatch*: the best match can be accessed using
        :meth:`Region.getLastMatch` afterwards.

        Note: You may adjust the scan rate (how often a search during the wait
        takes place) by setting :py:attr:`Settings.WaitScanRate` appropriately.
        """
        if PS is not None:
            assert_PS(PS, self.wait)
        if seconds is not None and not seconds == 'FOREVER':
            assert_positive_num(seconds, self.wait)
    @wait.func
    def wait(self, PS=None, seconds=None):
        """
        :param PS: a :class:`~sikuli_client.pattern.Pattern` object or a string
            (path to an image file or just plain text)
        :param seconds: a number, which can have a fraction, as maximum waiting
            time in seconds. The internal granularity is milliseconds. If not
            specified, the auto wait timeout value set by
            :py:meth:`Region.setAutoWaitTimeout` is used. Use the constant
            *FOREVER* to wait for an infinite time.
        :rtype: a :class:`~sikuli_client.match.Match` object that contains the
            best match or fails if PatternNotFound
        """
        if PS is None:
            from time import sleep
            sleep(seconds)
            return
        ps_str = PS._str_get if isinstance(PS, SikuliClass) else PS
        if seconds is None:
            sec_str = repr(self.getAutoWaitTimeout())
        elif isinstance(seconds, int):
            sec_str = repr(seconds)
        else:
            sec_str = seconds
        match_id = self.remote._eval(
            "self._new_jython_object(self._get_jython_object(%r).wait("
            "PS=%s, seconds=%s))" % (self._id, ps_str, sec_str))
        return Match(remote=self.remote, server_id=match_id)

    @run_on_remote
    def waitVanish(self, PS, seconds=None):
        """
        :param PS: a :class:`~sikuli_client.pattern.Pattern` object or a string
            (path to an image file or just plain text)
        :param seconds: a number, which can have a fraction, as maximum waiting
            time in seconds. The internal granularity is milliseconds. If not
            specified, the auto wait timeout value set by
            :py:meth:`Region.setAutoWaitTimeout` is used. Use the string
            *'FOREVER'* to wait for an infinite time.
        :rtype: *True* if the pattern vanishes within the specified waiting
            time, or *False* if the pattern stays visible after the waiting
            time has elapsed.

        This method keeps searching the given pattern in the region until the
        image vanishes (can not be found with :py:meth:`Region.find` any
        longer) or the specified amount of time has elapsed. At least one find
        operation is performed, even if 0 seconds is specified.

        **Note**: You may adjust the scan rate (how often a search during the
        wait
        takes place) by setting :py:attr:`Settings.WaitScanRate` appropriately.
        """
        assert_PS(PS, self.waitVanish)
        if seconds is not None and not seconds == 'FOREVER':
            assert_positive_num(seconds, self.waitVanish)

    @wait.func
    def waitVanish(self, PS, seconds=None):
        """
        :param PS: a :class:`~sikuli_client.pattern.Pattern` object or a string
            (path to an image file or just plain text)
        :param seconds: a number, which can have a fraction, as maximum waiting
            time in seconds. The internal granularity is milliseconds. If not
            specified, the auto wait timeout value set by
            :py:meth:`Region.setAutoWaitTimeout` is used. Use the string
            *'FOREVER'* to wait for an infinite time.
        :rtype: *True* if the pattern vanishes within the specified waiting
            time, or *False* if the pattern stays visible after the waiting
            time has elapsed.
        """
        ps_str = PS._str_get if isinstance(PS, SikuliClass) else PS
        if seconds is None:
            sec_str = repr(self.getAutoWaitTimeout())
        elif isinstance(seconds, int):
            sec_str = repr(seconds)
        else:
            sec_str = seconds
        return self.remote._eval("self._get_jython_object(%r).waitVanish(PS=%s,"
                                 " seconds=%s)" % (self._id, ps_str, sec_str))

    @run_on_remote
    def exists(self, PS, seconds=None):
        """
        Check whether the give pattern is visible on the screen.

        :param PS: a :py:class:`Pattern` object or a string (path to an image
            file or just plain text)
        :param seconds: a number, which can have a fraction, as maximum waiting
            time in seconds. The internal granularity is milliseconds. If not
            specified, the auto wait timeout value set by
            :py:meth:`Region.setAutoWaitTimeout` is used. Use the constant
            *FOREVER* to wait for an infinite time.
        :rtype: a :class:`~sikuli_client.match.Match` object that contains the
            best match or fails if PatternNotFound. None is returned, if nothing
            is found within the specified waiting time.

        Does exactly the same as :py:meth:`Region.wait()`, but no exception is
        raised in case of FindFailed. So it can be used to symplify scripting
        in case that you only want to know wether something is there or not to
        decide how to proceed in your workflow. So it is typically used with an
        if statement.  At least one find operation is performed, even if 0
        seconds is specified. So specifying 0 seconds saves some time, in case
        there is no need to wait, since its your intention to get the
        information "not found" directly.

        **Side Effect** *lastMatch*: the best match can be accessed using
        :py:meth:`Region.getLastMatch` afterwards.

        **Note**: You may adjust the scan rate (how often a search during the
        wait
        takes place) by setting :py:attr:`Settings.WaitScanRate` appropriately.
        """
        assert_PS(PS, self.exists)
        if seconds is not None and not seconds == 'FOREVER':
            assert_positive_num(seconds, self.exists)

    @exists.func
    def exists(self, PS, seconds=None):
        """
        :param PS: a :py:class:`Pattern` object or a string (path to an image
            file or just plain text)
        :param seconds: a number, which can have a fraction, as maximum waiting
            time in seconds. The internal granularity is milliseconds. If not
            specified, the auto wait timeout value set by
            :py:meth:`Region.setAutoWaitTimeout` is used. Use the constant
            *FOREVER* to wait for an infinite time.
        :rtype: a :class:`~sikuli_client.match.Match` object that contains the
            best match or fails if PatternNotFound. None is returned, if nothing
            is found within the specified waiting time.
        """
        ps_str = PS._str_get if isinstance(PS, SikuliClass) else PS
        if seconds is None:
            sec_str = repr(self.getAutoWaitTimeout())
        elif isinstance(seconds, int):
            sec_str = repr(seconds)
        else:
            sec_str = seconds
        match_id = self.remote._eval(
            "self._new_jython_object(self._get_jython_object(%r)"
            ".exists(PS=%s, seconds=%s))" % (self._id, ps_str, sec_str))
        return (Match(remote=self.remote, server_id=match_id) if match_id is not
                None else match_id)

    @DEFERRED
    def onAppear(self):
        """
        .. todo:: Implement
        """
        pass

    @DEFERRED
    def onVanish(self):
        """
        .. todo:: Implement
        """
        pass

    @DEFERRED
    def onChange(self):
        """
        .. todo:: Implement
        """
        pass

    @DEFERRED
    def observe(self):
        """
        .. todo:: Implement
        """
        pass

    @DEFERRED
    def stopObserver(self):
        """
        .. todo:: Implement
        """
        pass

    @TODO
    def click(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def doubleClick(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def rightClick(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    #60%
    @TODO
    def highlight(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def hover(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def dragDrop(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def drag(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def dropAt(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    #70%
    @TODO
    def type(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def paste(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def text(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def mouseDown(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def mouseUp(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    #80%
    @TODO
    def mouseMove(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def wheel(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def keyDown(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def keyUp(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def setFindFailedResponse(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    #90%
    @TODO
    def getFindFailedResponse(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def setThrowException(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def getThrowException(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
    def getRegionFromPSRM(self):
        """
        .. todo:: Implement
        """
        #TODO
        pass

    @TODO
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
