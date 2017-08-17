import argparse
import os
from pkget import PkgetError
from .utils import update_value


class Config():
    def __init__(self):
        self.recipepaths = []
        self.recipepaths.append(
            self.abspath(
                os.path.join(os.path.dirname(__file__), "recipes")))
        self.installprefix = ""
        self.pkginfoprefix = ""

        self.globally = False
        self.install = True
        self.uninstall = False
        self.configfiles = [self.abspath("~/.pkget.yaml")]

    def __str__(self):
        return str({"recipepaths": self.recipepaths,
                    "installprefix": self.installprefix,
                    "pkginfoprefix": self.pkginfoprefix,
                    "globally": self.globally,
                    "install": self.install,
                    "uninstall": self.uninstall,
                    "configfiles": self.configfiles})

    def parseArguments(self, args):
        pass

    def update_value(self, name, config, merge_value=True,
                     ignore_empty=True, ignore_false=True,
                     ignore_none=True):
        if isinstance(config, list):
            raise PkgetError("config is not list", "config")
        kwargs = {"ignore_empty": ignore_empty,
                  "ignore_false": ignore_false,
                  "ignore_none": ignore_none,
                  "merge_value": merge_value}
        value = None
        if isinstance(config, dict):
            if not (name in config):
                return
            value = config[name]
        else:
            if not hasattr(config, name):
                return
            value = getattr(config, name)
        return update_value(self, name, value, **kwargs)

    def abspath(self, path):
        if not path:
            return ""
        return os.path.abspath(
            os.path.expandvars(os.path.expanduser(path)))

    def update_config(self, config):
        self.update_value("recipepaths", config)
        self.update_value("installprefix", config, merge_value=False)
        self.update_value("pkginfoprefix", config, merge_value=False)
        self.update_value("globally", config, ignore_empty=False,
                          ignore_false=False)
        self.update_value("install", config, ignore_empty=False,
                          ignore_false=False)
        self.update_value("uninstall", config, ignore_empty=False,
                          ignore_false=False)
        self.update_value("configfiles", config)

        self.installprefix = self.abspath(self.installprefix)
        self.pkginfoprefix = self.abspath(self.pkginfoprefix)
        for i in range(len(self.recipepaths)):
            self.recipepaths[i] = self.abspath(self.recipepaths[i])

        for i in range(len(self.configfiles)):
            self.configfiles[i] = self.abspath(self.configfiles[i])
