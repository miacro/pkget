#!/usr/bin/env python
from .basic_config import BasicConfig


class PackageConfig(BasicConfig):
    def __init__(self):
        super().__init__(
            attributes={"description": "",
                        "website": "",
                        "type": "",
                        "name": "",
                        "version": "",
                        "os": "linux",
                        "arch": "amd64",
                        "url": "",
                        "urlprefix": "",
                        "depends": []})

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
