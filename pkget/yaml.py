import os
import yaml
from .exception import PkgetError
from .utils import Utils


class Yaml():
    def __init__(self):
        pass

    def load(content):
        try:
            return yaml.load_all(content)
        except yaml.YAMLError as ex:
            raise PkgetError("error while load yaml", "yaml") from ex

    def load_all(contents=[], filenames=[]):
        if isinstance(contents, str):
            contents = [contents]
        elif contents is None:
            contents = []

        if isinstance(filenames, str):
            filenames = [filenames]
        elif filenames is None:
            filenames = []

        for content in contents:
            generator = Yaml.load(content)
            for item in generator:
                yield item

        for filename in filenames:
            with open(Utils.abspath(filename), "r") as stream:
                generator = Yaml.load(stream)
                for item in generator:
                    yield item
