import os
from .exception import PkgetError
from .utils import update_value, abspath
from .basic_config import BasicConfig


class GlobalConfig(BasicConfig):
    def __init__(self):
        super().__init__(
            attributes={"recipepaths": [],
                        "installprefix": "",
                        "pkginfoprefix": ""})
        self.recipepaths.append(
            abspath(
                os.path.join(os.path.dirname(__file__), "recipes")))

    def update_config(self, *args, **kwargs):
        super().update_config(*args, **kwargs)
        self.installprefix = abspath(self.installprefix)
        self.pkginfoprefix = abspath(self.pkginfoprefix)
        for i in range(len(self.recipepaths)):
            self.recipepaths[i] = abspath(self.recipepaths[i])
