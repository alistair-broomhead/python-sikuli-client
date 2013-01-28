"""
Classes to fulfill the roles of those described at
    http://doc.sikuli.org/screen.html
"""
from .sikuli_class import ClientSikuliClass
from .misc import (constructor,
                   run_on_remote,
                   DEFERRED)
from .asserts import (assert_Region)
__author__ = 'Alistair Broomhead'


class Screen(ClientSikuliClass):
    """
    Manages interaction with Sikuli's Screen, reflecting
    http://doc.sikuli.org/screen.html#Screen
    """

    @run_on_remote
    def getNumberScreens(self):
        """
        Get the number of screens in a multi-monitor environment at the time
        the script is running.

        :rtype: int
        """
        pass

    @run_on_remote
    def getBounds(self):
        """
        Get the dimensions of monitor represented by the screen object.

        The width and height of the rectangle denote the dimensions of the
        monitor represented by the screen object. These attributes are obtained
        from the operating system. They can not be modified using Sikuli script.

        :rtype: (int, int, int, int)
        """
        pass

    @getBounds.func
    def getBounds(self):
        """
        :rtype: (int, int, int, int)
        """
        gb = "self._get_jython_object(%r).getBounds()" % self._id
        return self.remote._eval("[(x.x, x.y, x.width, x.height) "
                                 "for x in [%s]][0]" % gb)

    @run_on_remote
    def capture(self, *args):
        """
        Get the dimensions of monitor represented by the screen object.

        The width and height of the rectangle denote the dimensions of the
        monitor represented by the screen object. These attributes are obtained
        from the operating system. They can not be modified using Sikuli script.

        :param args: (Region,) | (x, y, w, h)
        :rtype: str
        """
        if len(args) == 1:
            assert_Region(args[0], self.capture)
        elif len(args) != 4:
            raise TypeError(
                "%r expected (x, y, w, h), got %r" % (self.capture, args))
        else:
            for a in zip('xywh', args):
                if not isinstance(a, int) or a <= 0:
                    raise TypeError(
                        "%r expected positive integers for each of "
                        "(x, y, w, h), got %r" % (self.capture, args))

    @DEFERRED
    def selectRegion(self, text=None):
        """
        Select a region on the screen interactively

        text is displayed for about 2 seconds in the middle of the screen. If
        text is omitted, the default "Select a region on the screen" is
        displayed.

        The interactive capture mode is entered and allows the user to select a
        region the same way as using the selection tool in the IDE.

        Note: You should check the result, since the user may cancel the
        capturing.

        :rtype : Region object or None, if the user cancels the capturing
            process.
        :param text: Text to display in the middle of the screen.
        """
        pass


@constructor(Screen)
def _screen_constructor(id_=0):
    return "Sikuli.Screen(%r)" % id_

