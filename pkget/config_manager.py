import yaml
from .global_config import GlobalConfig
from .package import Package
from .exception import PkgetError


class ConfigManager():
    def __init__(self, configfiles=[]):
        self.global_config = GlobalConfig()
        self.packages = []

    def load_yaml(self, filename):
        try:
            with open(filename, "r") as stream:
                generator = yaml.load_all(stream)
                contents = []
                for content in generator:
                    contents.append(content)
                return contents
        except yaml.YAMLError as ex:
            raise PkgetError("error while load yaml", "config") from ex
