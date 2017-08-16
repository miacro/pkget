#!/usr/bin/env python
from pkget import Config

config = Config()
config.update_config({
    "installprefix": "~/.local",
    "pkginfoprefix": "~",
    "recipepaths": ["~/.local", "", None],
})
print(config)
config.update_config({
    "installprefix": None,
    "globally": True,
    "install": False,
    "uninstall": True,
    "configfiles": ["~/.local", "~", None, ""]
})
print(config)
