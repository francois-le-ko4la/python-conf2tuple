#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 ######  #####   #####    ####   #####
 #       #    #  #    #  #    #  #    #
 #####   #    #  #    #  #    #  #    #
 #       #####   #####   #    #  #####
 #       #   #   #   #   #    #  #   #
 ######  #    #  #    #   ####   #    #

"""


class NamedTupleConfigError(Exception):
    """
    Generic exception.
    """
    pass


class NamedTupleConfigFileNotFound(NamedTupleConfigError):
    """
    Config file is not found
    """
    def __init__(self, value):
        super().__init__("File \"{}\" not found!".format(value))


class NamedTupleConfigLoadError(NamedTupleConfigError):
    """
    Content cannot be loaded.
    """
    def __init__(self):
        super().__init__("Can't load the configuration...")


__all__ = [
    'NamedTupleConfigError',
    'NamedTupleConfigFileNotFound',
    'NamedTupleConfigLoadError'
]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
