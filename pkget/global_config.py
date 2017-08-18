import os
from .utils import Utils
from .basic_config import BasicConfig


class GlobalConfig(BasicConfig):
    def __init__(self):
        super().__init__(
            attributes={"recipepaths": [],
                        "installprefix": "",
                        "pkginfoprefix": ""})
        self.recipepaths.append(
            Utils.abspath(
                os.path.join(os.path.dirname(__file__), "recipes")))

    def update_config(self, *args, **kwargs):
        super().update_config(*args, **kwargs)
        self.installprefix = Utils.abspath(self.installprefix)
        self.pkginfoprefix = Utils.abspath(self.pkginfoprefix)
        for i in range(len(self.recipepaths)):
            self.recipepaths[i] = Utils.abspath(self.recipepaths[i])
