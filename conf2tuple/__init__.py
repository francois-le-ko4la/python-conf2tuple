#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# conf2tuple
## Description:

This package loads the configuration values defined in external JSON or
YAML file, not the built-in data structures.

## Setup:

```shell
$ git clone https://github.com/francois-le-ko4la/python-conf2tuple.git
$ cd python-conf2tuple
$ make install
```

## Test:

This module has been tested and validated on Ubuntu.
```shell
$ make test
```

## Use:

```python
from conf2tuple import NamedTupleConfig
conf = "/path/to/the/file"
# NamedTupleConfig(path (str), NamedTupleConfig.{isjson|isyaml})
config = NamedTupleConfig(conf, NamedTupleConfig.isjson)
print(config)
```

## Project Structure
```
.
├── conf2tuple
│   ├── __about__.py
│   ├── config.py
│   ├── exceptions.py
│   ├── file.py
│   └── __init__.py
├── last_check.log
├── LICENSE
├── Makefile
├── pictures
│   ├── classes_conf2tuple.png
│   └── packages_conf2tuple.png
├── README.md
├── runtime.txt
├── setup.cfg
├── setup.py
└── tests
    ├── facebook.json
    ├── facebook.yaml
    ├── test_doctest.py
    └── test_pycodestyle.py
```

## Todo:

- [X] Create the project
- [X] Write code and tests
- [X] Test installation and requirements (setup.py and/or Makefile)
- [X] Test code
- [X] Validate features
- [X] Write Doc/stringdoc
- [X] Run PEP8 validation
- [X] Clean & last check
- [X] Fix global header
- [X] Fix tests
- [X] Fix doc
- [X] Release : 1.0.0

## License

This package is distributed under the [GPLv3 license](./LICENSE)

"""

from conf2tuple.__about__ import (
    __version__,
    __email__,
    __author__,
    __url__,
    __license__,
    FILENAME,
    DATA
)
from conf2tuple.exceptions import (
    NamedTupleConfigError,
    NamedTupleConfigFileNotFound,
    NamedTupleConfigLoadError
)
from conf2tuple.file import ConfigFile
from conf2tuple.config import NamedTupleConfig


__all__ = ["exceptions", "config", "file"]
