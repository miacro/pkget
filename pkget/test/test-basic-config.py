#!/usr/bin/env python
from pkget import BasicConfig

config = BasicConfig(attributes=
                     {"installprefix": None,
                      "pkginfoprefix": None,
                      "recipepaths": [],
                      "globally": False,
                      "install": True,
                      "uninstall": False,
                      "configfiles": []})
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
    "globally": True,
    "install": False,
    "uninstall": True,
    "configfiles": ["~/.local", "~", None, ""]
})
print(config)

for key, value in config:
    print(key, value)
