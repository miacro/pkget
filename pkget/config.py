import argparse
import os
from pkget import PkgetError
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

    def merge_value(self, name, config, ignore_empty=True):
        if not (name in config):
            return
        if not config[name]:
            return

        if isinstance(getattr(self, name), list):
            if not isinstance(config[name], list):
                raise PkgetError("value of %s is not list" % name,
                                 "config")
            for i in config[name]:
                if (not ignore_empty) or i:
                    getattr(self, name).append(i)

        elif isinstance(getattr(self, name), dict):
            if not isinstance(config[name], dict):
                raise PkgetError("value of %s is not dict" % name,
                                 "config")
            for i in config[name]:
                if (not ignore_empty) or config[name][i]:
                    getattr(self, name)[i] = config[name][i]
        else:
            raise PkgetError(
                "value of %s is not list or dict" % name,
                "config")

    def override_value(self, name, config, ignore_empty=True):
        if not (name in config):
            return

        if config[name] is None:
            return

        if (not ignore_empty) or config[name]:
            setattr(self, name, config[name])

    def abspath(self, path):
        if not path:
            return ""
        return os.path.abspath(
            os.path.expandvars(os.path.expanduser(path)))

    def update_config(self, config):
        self.merge_value("recipepaths", config)
        self.override_value("installprefix", config)
        self.override_value("pkginfoprefix", config)
        self.override_value("globally", config, ignore_empty=False)
        self.override_value("install", config, ignore_empty=False)
        self.override_value("uninstall", config, ignore_empty=False)
        self.merge_value("configfiles", config)

        self.installprefix = self.abspath(self.installprefix)
        self.pkginfoprefix = self.abspath(self.pkginfoprefix)
        for i in range(len(self.recipepaths)):
            self.recipepaths[i] = self.abspath(self.recipepaths[i])

        for i in range(len(self.configfiles)):
            self.configfiles[i] = self.abspath(self.configfiles[i])
