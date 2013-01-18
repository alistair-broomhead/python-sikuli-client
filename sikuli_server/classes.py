"""
Server-side classes

- :class:`~sikuli_server.class_definitions.finder.Finder`
- :class:`~sikuli_server.class_definitions.globals.Settings`
- :class:`~sikuli_server.class_definitions.globals.App`
- :class:`~sikuli_server.class_definitions.globals.Env`
- :class:`~sikuli_server.class_definitions.globals.Vision`
- :class:`~sikuli_server.class_definitions.match.Match`
- :class:`~sikuli_server.class_definitions.pattern.Pattern`
- :class:`~sikuli_server.class_definitions.region.SikuliEvent`
- :class:`~sikuli_server.class_definitions.region.Region`
- :class:`~sikuli_server.class_definitions.screen.Screen`
"""
from .class_definitions.finder import Finder
from .class_definitions.globals import Settings, App, Env, Vision
from .class_definitions.match import Match
from .class_definitions.pattern import Pattern
from .class_definitions.region import SikuliEvent, Region
from .class_definitions.screen import Screen

SIKULI_CLASSES = {}
for cls in [
    Finder,
    Settings, App, Env, Vision,
    Match,
    Pattern,
    SikuliEvent, Region,
    Screen
]: SIKULI_CLASSES[cls.__name__] = cls
