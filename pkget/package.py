#!/usr/bin/env python
import yaml
from pkget.utils import update_value


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

    def __str__(self):
        return str({"description": self.description,
                    "website": self.website,
                    "type": self.type,
                    "name": self.name,
                    "version": self.version,
                    "os": self.os,
                    "arch": self.arch,
                    "url": self.url,
                    "urlprefix": self.urlprefix,
                    "depends": self.depends})

    def update_value(self, name, config, *args, **kwargs):
        if not (name in config):
            return
        if isinstance(getattr(self, name), list):
            setattr(self, name, [])
        elif isinstance(getattr(self, name), dict):
            setattr(self, name, {})
        update_value(self, name, config[name], *args, **kwargs)

    def update_config(self, config):
        self.update_value("description", config)
        self.update_value("type", config)
        self.update_value("name", config)
        self.update_value("version", config)
        self.update_value("os", config)
        self.update_value("arch", config)
        self.update_value("url", config)
        self.update_value("urlprefix", config)
        self.update_value("website", config)
        self.update_value("depends", config, merge_value=True)

    def init_from_yaml(self, filename):
        with open(filename, "r") as stream:
            try:
                pkg = yaml.load(stream)
                self.update_config(pkg["package"])
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
