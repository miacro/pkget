#!/usr/bin/env python
import yaml

class Package():
    def __init__(self, configfile="", type=""):
        self.description = ""
        self.website = ""
        self.type = ""
        self.name = ""
        self.version = ""
        self.os = "linux"
        self.arch = "amd64"
        self.url = ""
        self.urlprefix = ""
        self.depends = []
        if type == "yaml":
            self.init_from_yaml(configfile)

    def _override_config(self, config):
        def _override_value(name):
            if name in config and config[name]:
                setattr(self, name, config[name])

        _override_value("description")
        _override_value("type")
        _override_value("name")
        _override_value("version")
        _override_value("os")
        _override_value("arch")
        _override_value("url")
        _override_value("urlprefix")
        _override_value("website")

    def init_from_yaml(self, filename):
        with open(filename, "r") as stream:
            try:
                pkg = yaml.load(stream)
                self._override_config(pkg["package"])
            except yaml.YAMLError as ex:
                raise ex

    def get_url(self):
        if self.url:
            return self.url
        if not self.urlprefix:
            return ""
        url = self.urlprefix
        if url[-1] != "/":
            url += "/"
        url += "v%s/%s-v%s-%s-%s" % \
            (self.version, self.name, self.version, self.os, self.arch)
        if self.type == "tar.gz":
            url += ".tar.gz"
        return url
