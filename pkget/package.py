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

    def update_config(self, config):
        update_value(self, "description", config["description"])
        update_value(self, "type", config["type"])
        update_value(self, "name", config["name"])
        update_value(self, "version", config["version"])
        update_value(self, "os", config["os"])
        update_value(self, "arch", config["arch"])
        update_value(self, "url", config["url"])
        update_value(self, "urlprefix", config["urlprefix"])
        update_value(self, "website", config["website"])
        update_value(self, "depends", config["depends"], merge_value=False)

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
