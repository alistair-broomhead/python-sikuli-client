"""
Server-side classes
"""
from .finder import Finder
from .globals import Settings, App, Env, Vision
from .match import Match
from .pattern import Pattern
from .region import SikuliEvent, Region
from .screen import Screen

SIKULI_CLASSES = {}
for cls in [
    Finder, Settings, App, Env, Vision, Match, SikuliEvent, Region, Screen
]: SIKULI_CLASSES[cls.__name__] = cls
