"""
All the client-side Sikuli objects

- :class:`~python_sikuli_client.finder.Finder`
- :class:`~python_sikuli_client.globals.Settings`
- :class:`~python_sikuli_client.globals.App`
- :class:`~python_sikuli_client.globals.Env`
- :class:`~python_sikuli_client.globals.Vision`
- :class:`~python_sikuli_client.match.Match`
- :class:`~python_sikuli_client.pattern.Pattern`
- :class:`~python_sikuli_client.region.SikuliEvent`
- :class:`~python_sikuli_client.region.Region`
- :class:`~python_sikuli_client.screen.Screen`
"""
__author__ = 'Alistair Broomhead'

from python_sikuli_client.finder import Finder
from python_sikuli_client.globals import Settings, App, Env, Vision
from python_sikuli_client.match import Match
from python_sikuli_client.pattern import Pattern
from python_sikuli_client.region import SikuliEvent, Region
from python_sikuli_client.screen import Screen
from python_sikuli_client.location import Location

SIKULI_CLASSES = {
    cls.__name__: cls
    for cls in [Finder,
                Settings, App, Env, Vision,
                Match,
                Pattern,
                SikuliEvent, Region,
                Screen,
                Location
    ]
}
