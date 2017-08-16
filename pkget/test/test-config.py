#!/usr/bin/env python
from pkget import Config

config = Config()
config.update_config({"installprefix": "~/.local",
                      "recipepaths": ["~/.local"]})
print(config)
