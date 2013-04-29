"""

:class:`Region` and :class:`SikuliEvent` classes to fulfill the roles of those
described at http://doc.sikuli.org/region.html

.. toctree::
   :maxdepth: 2

"""
from .asserts import (assert_positive_int,
                      assert_PS,
                      assert_PSMRL,
                      assert_positive_num,
                      assert_PSRM)
from .misc import (dropNones,
                   constructor,
                   return_from_remote,
                   DEFERRED,
                   TODO,
                   run_on_remote)

__author__ = 'Alistair Broomhead'
from .sikuli_class import (UnimplementedSikuliClass,
                           SikuliClass)


class SikuliEvent(UnimplementedSikuliClass):
    """
    Manages interaction with Sikuli's SikuliEvent, reflecting
    http://doc.sikuli.org/region.html#SikuliEvent

    .. todo:: Implement

    """
    #TODO: SikuliEvent class
    pass


#noinspection PyUnusedLocal
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
        :param location: :class:`~sikuli_client.location.Location` - the new top
            left corner
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

    @return_from_remote('Location')
    def getCenter(self):
        """
        :rtype: :class:`~sikuli_client.location.Location`

        Get the center of the region.
        """
        pass

    @return_from_remote('Location')
    def getTopLeft(self):
        """
        :rtype: :class:`~sikuli_client.location.Location`

        Get the location of the region's respective corner.
        """
        pass

    @return_from_remote('Location')
    def getTopRight(self):
        """
        :rtype: :class:`~sikuli_client.location.Location`

        Get the location of the region's respective corner.
        """
        pass

    @return_from_remote('Location')
    def getBottomLeft(self):
        """
        :rtype: :class:`~sikuli_client.location.Location`

        Get the location of the region's respective corner.
        """
        pass

    @return_from_remote('Location')
    def getBottomRight(self):
        """
        :rtype: :class:`~sikuli_client.location.Location`

        Get the location of the region's respective corner.
        """
        pass

    @return_from_remote('Screen')
    def getScreen(self):
        """
        :rtype: :class:`~sikuli_client.screen.Screen`

        Returns the screen object that contains this region.

        This method only makes sense in Multi Monitor Environments, since it
        always returns the default screen in a single monitor environment.
        """
        pass

    @return_from_remote('Match')
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
        from .match import Match
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
        assert_positive_int(range_px, self.nearby)

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

    @return_from_remote('Match')
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
        from .match import Match
        return (Match(remote=self.remote, server_id=match_id)
                for match_id in match_ids)

    @return_from_remote('Match')
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
        from .match import Match
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

        from .match import Match
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

    @run_on_remote
    def click(self, PSMRL, modifiers=None):
        """
        Perform a mouse click on the click point using the left button.

        :param PSMRL: a pattern, a string, a match, a region or a location that
            evaluates to a click point.

        :param modifiers: key modifiers

        :rtype: the number of performed clicks (actually 1). A 0 (integer null)
            means that because of some reason, no click could be performed (in
            case of *PS* may be PatternNotFound).

        **Side Effect** if *PS* was used, the match can be accessed using
        :py:meth:`Region.getLastMatch` afterwards.

        **Example:**

        .. code-block:: python

            # Windows XP
            click("xpstart.png")

            # Windows Vista
            click("vistastart.png")

            # Windows 7
            click("w7start.png")

            # Mac
            click("apple.png")
        """
        assert_PSMRL(PSMRL, self.click)

    @click.arg
    def click(self, PSMRL, modifiers=None):
        """
        :param PSMRL: a pattern, a string, a match, a region or a location that
            evaluates to a click point.

        :param modifiers: key modifiers

        """
        return dropNones(1, None, PSMRL, modifiers)

    @run_on_remote
    def doubleClick(self, PSMRL, modifiers=None):
        """
        Perform a mouse double-click on the click point using the left button.

        :param PSMRL: a pattern, a string, a match, a region or a location that
            evaluates to a click point.

        :param modifiers: one or more key modifiers

        :rtype: the number of performed double-clicks (actually 1). A 0 (
            integer null) means that because of some reason, no click could be
            performed (in case of *PS* may be PatternNotFound).

        **Side Effect** if *PS* was used, the match can be accessed using
        :py:meth:`Region.getLastMatch` afterwards.
        """
        assert_PSMRL(PSMRL, self.doubleClick)

    @doubleClick.arg
    def doubleClick(self, PSMRL, modifiers=None):
        """
        :param PSMRL: a pattern, a string, a match, a region or a location that
            evaluates to a click point.

        :param modifiers: one or more key modifiers
        """
        return dropNones(1, None, PSMRL, modifiers)

    @run_on_remote
    def rightClick(self, PSMRL, *modifiers):
        """
        Perform a mouse click on the click point using the right button.

        :param PSMRL: a pattern, a string, a match, a region or a location that
            evaluates to a click point.

        :param modifiers: one or more key modifiers

        :rtype: the number of performed double-clicks (actually 1). A 0 (
            integer null) means that because of some reason, no c

        **Side Effect** if *PS* was used, the match can be accessed using
        :py:meth:`Region.getLastMatch` afterwards.
        """
        assert_PSMRL(PSMRL, self.doubleClick)

    @run_on_remote
    def highlight(self, seconds=None):
        """
        Highlight the region for some period of time.

        :param seconds: a decimal number taken as duration in seconds

        The region is highlighted showing a red colored frame around it. If the
        parameter seconds  is given, the script is suspended for the specified
        time. If no time is given, the highlighting is started and the script
        continues.

        When later on the same highlight call without a parameter is made, the
        highlighting is stopped (behaves like a toggling switch).

        Example::

            m = find(some_image)

            # the red frame will blink for about 7 - 8 seconds
            for i in range(5):
                m.highlight(1)
                wait(0.5)

            # a second red frame will blink as an overlay to the first one
            m.highlight()
            for i in range(5):
                m.highlight(1)
                wait(0.5)
            m.highlight()

            # the red frame will grow 5 times
            for i in range(5):
                m.highlight(1)
                m = m.nearby(20)

        **Note**: The red frame is just an overlay in front of all other screen
        content and stays in its place, independently from the behavior of this
        other content, which means it is not "connected" to the *content* of the
        defining region. But it will be adjusted automatically, if you change
        position and/or dimension of this region in your script, while it is
        highlighted.
        """
        pass

    @highlight.arg
    def highlight(self, seconds=None):
        """
        :param seconds: a decimal number taken as duration in seconds
        """
        return dropNones(0, None, seconds)

    @run_on_remote
    def hover(self, PSMRL, modifiers=None):
        """
        Move the mouse cursor to hover above a click point.

        :param PSMRL: a pattern, a string, a match, a region or a location that
            evaluates to a click point.

        :param modifiers: one or more key modifiers

        :rtype: the number 1 if the mousepointer could be moved to the click
            point. A 0 (integer null) returned means that because of some
            reason, no move could be performed (in case of *PS* may be
            PatternNotFound).

        **Side Effect** if *PS* was used, the match can be accessed using
        :py:meth:`Region.getLastMatch` afterwards.
        """
        assert_PSMRL(PSMRL, self.hover)

    @hover.arg
    def hover(self, PSMRL, modifiers=None):
        """
        :param PSMRL: a pattern, a string, a match, a region or a location that
            evaluates to a click point.
        :param modifiers: one or more key modifiers
        """
        return dropNones(1, None, PSMRL, modifiers)

    @run_on_remote
    def dragDrop(self, PSMRL_drag, PSMRL_drop, modifiers=None):
        """
        Perform a drag-and-drop operation from a starting click point to the
        target click point indicated by the two PSMRLs respectively.

        :param PSMRL_drag: a pattern, a string, a match, a region or a location
            that evaluates to a click point.

        :param PSMRL_drop: a pattern, a string, a match, a region or a location
            that evaluates to a click point.

        :param modifiers: one or more key modifiers

        If one of the parameters is *PS*, the operation might fail due to
        PatternNotFound.

        **Sideeffect**: when using *PS*, the match of the target can be accessed
        using :py:meth:`Region.getLastMatch` afterwards. If only the first
        parameter is given as *PS*, this match is returned by
        :py:meth:`Region.getLastMatch`.

        **When the operation does not perform as expected** (usually caused by
        timing problems due to delayed reactions of applications), you may
        adjust the internal timing parameters :py:attr:`Settings.DelayAfterDrag`
        and :py:attr:`Settings.DelayBeforeDrop` eventually combined with the
        internal timing parameter :py:attr:`Settings.MoveMouseDelay`.

        Another solution might be, to use a combination of
        :py:meth:`Region.drag` and :py:meth:`Region.dropAt` combined with your
        own ``wait()`` usages. If the mouse movement from source to target is
        the problem, you might break up the move path into short steps using
        :py:meth:`Region.mouseMove`.
        """
        assert_PSMRL(PSMRL_drag, self.dragDrop)
        assert_PSMRL(PSMRL_drop, self.dragDrop)

    @dragDrop.arg
    def dragDrop(self, PSMRL_drag, PSMRL_drop, modifiers=None):
        """
        :param PSMRL_drag: a pattern, a string, a match, a region or a location
            that evaluates to a click point.

        :param PSMRL_drop: a pattern, a string, a match, a region or a location
            that evaluates to a click point.

        :param modifiers: one or more key modifiers
        """
        return dropNones(2, None, PSMRL_drag, PSMRL_drop, modifiers)

    @run_on_remote
    def drag(self, PSMRL):
        """
        Start a drag-and-drop operation by dragging at the given click point.

        :param PSMRL: a pattern, a string, a match, a region or a location that
            evaluates to a click point.

        :rtype: the number 1 if the operation could be performed. A 0 (integer
            null) returned means that because of some reason, no move could be
            performed (in case of *PS* may be PatternNotFound).

        The mousepointer is moved to the click point and the left mouse
        button is pressed and held, until another mouse action is performed
        (e.g. a :py:meth:`Region.dropAt()` afterwards). This is nomally used to
        start a drag-and-drop operation.

        **Side Effect** if *PS* was used, the match can be accessed using
        :py:meth:`Region.getLastMatch` afterwards.
        """
        assert_PSMRL(PSMRL, self.drag)

    @run_on_remote
    def dropAt(self, PSMRL, delay=None):
        """
        Complete a drag-and-drop operation by dropping a previously dragged
        item at
        the given target click point.

        :param PSMRL: a pattern, a string, a match, a region or a location that
            evaluates to a click point.

        :param delay: time to wait after in seconds as decimal value

        :rtype: the number 1 if the operation could be performed. A 0
            (integer null) returned means that because of some reason, no move
            could be performed (in case of *PS* may be PatternNotFound).

        The mousepointer is moved to the click point. After waiting for delay
        seconds the left mouse button is released. This is normally used to
        finalize
        a drag-and-drop operation. If it is necessary to visit one ore more
        click
        points after dragging and before dropping, you can use
        :py:meth:`Region.mouseMove` inbetween.

        **Side Effect** if *PS* was used, the match can be accessed using
        :py:meth:`Region.getLastMatch` afterwards.
        """
        assert_PSMRL(PSMRL, self.dropAt)

    @dropAt.arg
    def dropAt(self, PSMRL, delay=None):
        """
        Complete a drag-and-drop operation by dropping a previously dragged
        item at
        the given target click point.

        :param PSMRL: a pattern, a string, a match, a region or a location that
            evaluates to a click point.

        :param delay: time to wait after in seconds as decimal value

        :rtype: the number 1 if the operation could be performed. A 0
            (integer null) returned means that because of some reason, no move
            could be performed (in case of *PS* may be PatternNotFound).
        """
        return dropNones(1, None, PSMRL, delay)

    #noinspection PyUnusedLocal,PyDocstring
    @run_on_remote
    def type(self, *args, **kwargs):
        """
        Type the text at the current focused input field or at a click point
        specified by *PSMRL*.

        :param PSMRL: a pattern, a string, a match, a region or a location that
            evaluates to a click point.

        :param text: a string to type.

        :param modifiers: one or more key modifiers

        :rtype: the number 1 if the operation could be
            performed, otherwise 0 (integer null), which means,
            that because of some reason, it was not possible or the click
            could be performed (in case of *PS* may be PatternNotFound).

        This method simulates keyboard typing interpreting the characters of
        text
        based on the layout/keymap of the **standard US keyboard (QWERTY)**.
        Special keys (ENTER, TAB, BACKSPACE, ...) can be incorporated into text
        by using the constants defined in
        `Class Key <http://doc.sikuli.org/keys.html>`_ using the standard
        string concatenation (+).

        If *PSMRL* is given, a click on the clickpoint is performed before
        typing, to gain the focus. (Mac: it might be necessary, to use
        :py:func:`switchApp` to give focus to a target application before, to
        accept typed/pasted characters.)

        If *PSMRL* is omitted, it performs the typing on the current focused
        visual component (normally an input field or an menu entry that can be
        selected by typing something).

        **Side Effect** if *PS* was used, the match can be accessed using
        :py:meth:`Region.getLastMatch` afterwards.

        **Note**: If you need to type international characters or you are using
        layouts/keymaps other than US-QWERTY, you should use
        :py:meth:`Region.paste` instead. Since type() is rather slow because it
        simulates each key press, for longer text it is preferrable to use
        :py:meth:`Region.paste`.

        **Best Practice**: As a general guideline, the best choice is to use
        ``paste()`` for readable text and ``type()`` for action keys like TAB,
        ENTER, ESC, ....
        Use one ``type()`` for each key or key combination and be aware,
        that in some cases a short ``wait()`` after a ``type()`` might be
        necessary to give the target application some time to react and be
        prepared for the next Sikuli action.
        """
        # Why would anyone in their right mind put optional args in front of
        # mandatory ones? I hope you know I hate you, whoever you are...
        def _raise_error():
            raise TypeError("Incorrect call signature for method %r. args=%r, "
                            "kwargs=%r:\n%s"
                            % (self.type, args, kwargs, self.type.__doc__))

        PSMRL = None
        text = None
        modifiers = None
        if kwargs:
            for k in kwargs:
                if k not in ('text', 'PSMRL', 'modifiers'):
                    _raise_error()
        if args and kwargs:
            if 'PSMRL' in kwargs:
                PSMRL = kwargs['PSMRL']
            if 'text' in kwargs:
                text = kwargs['text']
            if 'modifiers' in kwargs:
                modifiers = kwargs['modifiers']
            num_unset = len([x for x in (PSMRL, text, modifiers) if x is None])
            if len(args) > num_unset:
                _raise_error()
            if text is None:
                if PSMRL is not None:
                    text = args[0]
                elif not isinstance(args[0], basestring):
                    if len(args) == 1:
                        _raise_error()
                    elif len(args) == 2:
                        PSMRL, text = args
            elif not isinstance(args[0], basestring):
                PSMR = args[0]
            if PSMRL is not None:
                assert_PSMRL(PSMRL, self.type)
            return  # I'm screwwed
        elif args:
            if len(args) == 3:
                (PSMRL, text, modifiers) = args
            elif len(args) == 1:
                text = args[0]
            else:
                if not isinstance(args[0], basestring):
                    PSMRL, text = args
                else:
                    return  # pray to god as there's nothing I can do here...
        else:
            text = kwargs['text'] if 'text' in kwargs else None
            if 'PSMRL' in kwargs:
                PSMRL = kwargs['PSMRL']
        if PSMRL is not None:
            assert_PSMRL(PSMRL, self.type)
        if text is None or not isinstance(text, basestring):
            _raise_error()

    @run_on_remote
    def paste(self, PSMRL, text=None):
        """
        Paste the text at a click point.

        :param PSMRL: a pattern, a string, a match, a region or a location that
            evaluates to a click point.

        :param text: text to paste

        :rtype: the number 1 if the operation could be performed, otherwise 0
            (integer null), which means,
            that because of some reason, it was not possible or the click
            could be performed (in case of *PS* may be PatternNotFound).

        Pastes *text* using the clipboard (OS-level shortcut (Ctrl-V or
        Cmd-V)). So
        afterwards your clipboard contains *text*. ``paste()`` is a temporary
        solution for
        typing international characters or typing on keyboard layouts other
        than
        US-QWERTY.

        If *PSMRL* is given, a click on the clickpoint is performed before
        typing, to
        gain the focus. (Mac: it might be necessary,
        to use :py:func:`switchApp`
        to give focus to a target application before, to accept typed/pasted
        characters.)

        If *PSMRL* is omitted, it performs the paste on the current focused
        component
        (normally an input field).

        **Side Effect** if *PS* was used, the match can be accessed using
        :py:meth:`Region.getLastMatch` afterwards.

        **Note**: Special keys (ENTER, TAB, BACKSPACE, ...) cannot be used
        with ``paste()``.
        If needed, you have to split your complete text into two or more
        ``paste()``
        and use ``type()`` for typing the special keys inbetween.
        Characters like \\n    (enter/new line) and \\t (tab) should work as
        expected with ``paste()``,
        but be aware of timing problems, when using e.g. intervening \\t to
        jump
        to the next input field of a form.
        """
        pass

    @paste.arg
    def paste(self, PSMRL, text=None):
        """
        :param PSMRL: a pattern, a string, a match, a region or a location that
            evaluates to a click point.

        :param text: text to paste
        """
        return dropNones(1, None, PSMRL, text)

    @run_on_remote
    def text(self):
        """
        Extract the text contained in the region using OCR.

        :rtype: the text as a string.

        **Note**: Since this feature is still in an **experimental state**,
        be aware, that in some cases it might not work as expected. If you face
        any problems look at the
        `Questions & Answers / FAQ's <https://answers.launchpad .net/sikuli>`_
        and the `Bugs <https://answers.launchpad.net/sikuli>`_.
        """
        pass

    @run_on_remote
    def mouseDown(self, button):
        """
        Press the mouse *button* down.

        :param button: one or a combination of the button constants
            ``Button.LEFT``, ``Button.MIDDLE``, ``Button.RIGHT``.

        :rtype: the number 1 if the operation is performed successfully, and
            zero if otherwise.

        The mouse button or buttons specified by *button* are pressed until
        another
        mouse action is performed.
        """
        pass

    @run_on_remote
    def mouseUp(self, button=None):
        """
        Release the mouse button previously pressed.

        :param button: one or a combination of the button constants
            ``Button.LEFT``, ``Button.MIDDLE``, ``Button.RIGHT``.

        :rtype: the number 1 if the operation is performed successfully, and
            zero if otherwise.

        The button specified by *button* is released. If *button* is omitted,
        all currently pressed buttons are released.
        """
        pass

    @run_on_remote
    def mouseUp(self, button=None):
        """
        :param button: one or a combination of the button constants
        """
        dropNones(0, None, button)

    @run_on_remote
    def mouseMove(self, PSMRL):
        """
        Move the mouse pointer to a location indicated by PSRML.

        :param PSMRL: a pattern, a string, a match, a region or a location that
            evaluates to a click point.

        :rtype: the number 1 if the operation could be performed. If using *PS*
            (which invokes an implicity find operation), find fails and you have
            switched off FindFailed exception, a 0 (integer null) is returned.
            Otherwise, the script is stopped with a FindFailed exception.

        **Sideeffects**: when using *PS*, the match can be accessed using
        :py:meth:`Region.getLastMatch` afterwards
        """
        assert_PSMRL(PSMRL, self.mouseMove)

    @TODO
    def wheel(self):
        """
        .. todo:: Implement
        """
        pass

    @run_on_remote
    def keyDown(self, key):
        """
        Press and hold the specified key(s) until released by a later call to
        :py:meth:`Region.keyUp`.

        :param key: one or more keys (use the consts of class Key). A
            list of keys is a concatenation of several key constants using "+".

        :rtype: the number 1 if the operation could be performed and 0 if
            otherwise.
        """
        pass

    @run_on_remote
    def keyUp(self, key=None):
        """
        Release given keys. If no key is given, all currently pressed keys are
        released.

        :param key: one or more keys (use the consts of class Key). A
            list of keys is a concatenation of several key constants using "+".

        :rtype: the number 1 if the operation could be performed and 0 if
            otherwise.
        """
        pass

    @keyUp.arg
    def keyUp(self, key=None):
        """
        Release given keys. If no key is given, all currently pressed keys are
        released.

        :param key: one or more keys (use the consts of class Key). A
            list of keys is a concatenation of several key constants using "+".

        :rtype: the number 1 if the operation could be performed and 0 if
            otherwise.
        """
        return dropNones(0, None, key)

    @DEFERRED
    def setFindFailedResponse(self):
        """
        .. todo:: Implement
        """
        pass

    @DEFERRED
    def getFindFailedResponse(self):
        """
        .. todo:: Implement
        """
        pass

    @DEFERRED
    def setThrowException(self):
        """
        .. todo:: Implement
        """
        pass

    @DEFERRED
    def getThrowException(self):
        """
        .. todo:: Implement
        """
        pass

    @return_from_remote('Region')
    def getRegionFromPSRM(self, PSRM):
        """
        Returns a new Region object derived from the given parameter. In case
        of PS, internally a find() is done inside this region. If found,
        the match is returned. In case RM, just a copy of the given region is
        returned.

        :param PSRM: a Pattern, String, Region or Match object
        :rtype: a new Region object
        """
        assert_PSRM(PSRM, self.getRegionFromPSRM)

    @return_from_remote('Location')
    def getLocationFromPSRML(self, PSMRL):
        """
        Returns a new Location object derived from the given parameter. In
        case of PS, internally a find() is done inside this region. If found,
        the match's target offset position is returned. In case RM,
        just a copy of the given region's respective location (center or
        target offset) is returned.

        :param PSMRL: a Pattern, String, Region, Match or Location object
        :rtype: a new Location object
        """
        assert_PSMRL(PSMRL, self.getLocationFromPSRML)

    def get_xy_from_PSRML(self, PSMRL):
        from SikuliServer.sikuli_client.misc import s_repr

        r = "self._get_jython_object(%r)" % self._id
        l = "%s.getLocationFromPSRML(%s)" % (r, s_repr(PSMRL))
        cmd = "(lambda l: [l.getX(), l.getY()])(%s)" % l
        return self.remote._eval(cmd)

    def find_one_of(self, images):
        """
        :param images: list of strings giving paths to images
        :return: found images
        """
        from .match import Match
        match_ids = self.remote._eval_foreach(
            "self._new_jython_object(self._get_jython_object(%r).find(arg))"
            % self._id,
            images)
        from robot.api import logger
        matches = {}
        for (k, v) in sorted(match_ids.items(), key=lambda k: int(k[0])):
            img, match_id = v
            if match_id is None or not match_id:
                logger.debug("Did not find %r" % img)
            else:
                try:
                    matches[k] = Match(remote=self.remote, server_id=match_id)
                    logger.debug("Found %r" % img)
                except BaseException:
                    pass
        return matches

@constructor(Region)
def _region_constructor(x, y, w, h):
    return "Sikuli.Region(%r, %r, %r, %r)" % (x, y, w, h)


@constructor(Region)
def _region_constructor(region):
    return "Sikuli.Region(%s)" % region._str_get


@constructor(Region)
def _region_constructor():
    return ('Sikuli.Region('
            '   *(lambda x: [x.x, x.y, x.width, x.height])('
            '       Sikuli.SCREEN.getBounds()))')
