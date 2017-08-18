import yaml
from .global_config import GlobalConfig
from .package import Package
from .exception import PkgetError


class PackageManager():
    def __init__(self, configfiles=[]):
        self.global_config = {}
        self.packages = {}

    def update_global_config(self, config):
        pass
