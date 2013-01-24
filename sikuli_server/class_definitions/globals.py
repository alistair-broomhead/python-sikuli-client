"""
Classes to fulfill the roles of those described at
    http://doc.sikuli.org/globals.html
"""
__author__ = 'Alistair Broomhead'
from .sikuli_class import ServerSikuliClass

class Settings(ServerSikuliClass):
    """ Manages interaction with Sikuli's Settings """
    #TODO: Settings class
    # http://doc.sikuli.org/globals.html#Settings
    pass


class App(ServerSikuliClass):
    """ Manages interaction with Sikuli's App """
    #TODO: App class
    # http://doc.sikuli.org/globals.html#App
    pass


class Env(ServerSikuliClass):
    """ Manages interaction with Sikuli's Env """
    #TODO: Other Env. Info
    # http://doc.sikuli.org/globals.html#Env.getOS
    pass


class Vision(ServerSikuliClass):
    """ Manages interaction with Sikuli's Vision """
    #TODO: Tuning Vision Algorithm
    # http://doc.sikuli.org/globals.html#Vision.setParameter
    pass
