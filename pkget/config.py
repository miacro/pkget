import argparse
import os
class Config():
    def __init__(self):
        self.recipepaths = []
        self.recipepaths.append(
            os.path.abspath(
                os.path.join(os.path.dirname(__file__), "/recipes")))
        self.installprefix = ""
        self.pkginfoprefix = ""

        self.globally = False
        self.install = True
        self.uninstall = False
        self.configfile = os.path.abspath("~/.pkget.yaml")

    def parseArguments(self, args):
        pass

    def update_config(self, config, ignore_empty=True):
        def override_value(name):
            if (not ignore_empty) or \
                    (name in config and config[name]):
                setattr(self, name, config[name])

        def merge_value(name):
            if (not ignore_empty) or \
                    (name in config and config[name]):
                if isinstance(getattr(self, name), list):
                    pass
                elif isinstance(getattr(self, name), dict):
                    pass
                else:
                    pass

        override_value("description")
        override_value("type")
        override_value("name")
        override_value("version")
        override_value("os")
        override_value("arch")
        override_value("url")
        override_value("urlprefix")
        override_value("website")
