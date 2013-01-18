"""
Extra classes that implementent miscellaneous needed functionailty
"""

__author__ = 'Alistair Broomhead'
from .pattern import Pattern
from .match import Match


class RemoteLib(object):
    """ Re-exposes a classes keywords wrapped by robotremotelibrary.py """

    def __init__(self, remote):
        self.__lib = remote

    def __getattr__(self, name):
        if name in self.__lib.get_keyword_names():
            def _(*args):
                return self.__lib.run_keyword(name, args)

            _.__name__ = name
            self.__dict__[name] = _
            return _
        raise AttributeError()


class SikuliUnreflected(object):
    """ Custom keyword handlers rather than those reflected over RPC """

    def __init__(self, remote):
        """
        :type remote: SikuliServer
        """
        self.remote = remote

    def find(self, PS):
        """

        :param PS: :class:`~sikuli_client.pattern.Pattern` or str
        :rtype: :class:`~sikuli_client.match.Match`

        Find a particular GUI element, which is seen as the given image or
        just plain text. The given file name of an image specifies the
        element's appearance. It searches within the region and returns the best
        match, which shows a similarity greater than the minimum similarity
        given by the pattern. If no similarity was set for the pattern by
        :meth:`sikuli_client.pattern.Pattern.similar` before, a default minimum
        similarity of 0.7 is set automatically.

        If autoWaitTimeout is set to a non-zero value, find() just acts as a
        wait().

        **Side Effect** *lastMatch*: the best match can be accessed using
        :meth:`~sikuli_client.region.Region.getLastMatch` afterwards.
        """
        if isinstance(PS, Pattern):
            assert isinstance(PS, Pattern)
            ps = "self._get_jython_object(%r)" % PS.remote_id
        else:
            ps = repr(PS)
        match_id = self._eval("self._new_jython_object(self.find(%s))" % ps)
        return Match(remote=self.remote, id_=match_id)
