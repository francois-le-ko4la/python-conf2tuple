#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=R0903
"""

  ####    ####   #    #  ######
 #    #  #    #  ##   #  #
 #       #    #  # #  #  #####
 #       #    #  #  # #  #
 #    #  #    #  #   ##  #
  ####    ####   #    #  #

"""

import json
import yaml
from collections import namedtuple
from conf2tuple.__about__ import FILENAME, DATA
from conf2tuple.file import ConfigFile
from conf2tuple.exceptions import NamedTupleConfigLoadError


class NamedTupleConfig(namedtuple('NamedTupleConfig', ['filename', 'config'])):
    """
    This Class provides a namedtuple from a JSON File or YAML file.
    You can use it to avoid a lot of CONST in your scripts.

    Use:
        >>> # pathlib to run the test everywhere
        >>> import pathlib
        >>> path = str(pathlib.Path(__file__).resolve().parent) + "/"
        >>> cur_file = path + '../tests/facebook.json'
        >>> json = NamedTupleConfig(cur_file, NamedTupleConfig.isjson)
        >>> print(json.config)
        Config(description='Facebook APP API - create an application before \
using this profile', debug=True, data={'host': 'https://graph.facebook.com', \
'token': ['OAuth', 'XXXXX TOKEN XXXXX']})
        >>> cur_file = path + '../tests/facebook.yaml'
        >>> yaml = NamedTupleConfig(cur_file, NamedTupleConfig.isyaml)
        >>> yaml.config.data['host']
        'https://graph.facebook.com'
        >>> # oups 1: file not found
        >>> cur_file = '/etc/fst'
        >>> config = NamedTupleConfig(cur_file, NamedTupleConfig.isjson)
        Traceback (most recent call last):
        ...
        conf2tuple.exceptions.NamedTupleConfigFileNotFound: File "/etc/fst" \
not found!
        >>> # oups 2: can't load the file
        >>> cur_file = path + '../LICENSE'
        >>> config = NamedTupleConfig(cur_file, NamedTupleConfig.isjson)
        Traceback (most recent call last):
        ...
        conf2tuple.exceptions.NamedTupleConfigLoadError: Can't load the \
configuration...
    """

    def __new__(cls, filename, filetype):

        filename = ConfigFile(filename)
        loader = filetype()
        try:
            data = loader(filename.read())
        except ValueError:
            raise NamedTupleConfigLoadError()
        config = namedtuple('Config', data.keys())(*data.values())
        return super(NamedTupleConfig, cls).__new__(cls, str(filename), config)

    @staticmethod
    def isjson():
        """
        use it to define the file type
        """
        return json.loads

    @staticmethod
    def isyaml():
        """
        use it to define the file type
        """
        return yaml.load


if __name__ == "__main__":
    import doctest
    doctest.testmod()
