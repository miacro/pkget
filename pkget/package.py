#!/usr/bin/env python
from .utils import update_value
from .basic_config import BasicConfig


class Package(BasicConfig):
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
