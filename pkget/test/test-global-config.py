#!/usr/bin/env python
from pkget import GlobalConfig

config = GlobalConfig()
print("default")
print(config)
config.update_config({
    "installprefix": "~/.local",
    "pkginfoprefix": "~",
    "recipepaths": ["~/.local", "", None],
})
print(config)
config.update_config({
    "installprefix": None,
})
print(config)
