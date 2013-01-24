"""
Server-side classes
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
