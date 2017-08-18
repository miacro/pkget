from .exception import PkgetError
from .utils import update_value


class BasicConfig():
    def __init__(self, attributes):
        self.__attributes = {}
        if isinstance(attributes, dict):
            for i in attributes:
                if isinstance(attributes[i], dict):
                    self.__attributes[i] = attributes[i]
                else:
                    self.__attributes[i] = {"default": attributes[i]}
        elif isinstance(attributes, list):
            for i in attributes:
                self.__attributes[i] = {}

        for i in self.__attributes:
            if not ("default" in self.__attributes[i]):
                self.__attributes[i]["default"] = ""
            setattr(self, i, self.__attributes[i]["default"])

    def __iter__(self):
        for i in self.__attributes:
            yield i, getattr(self, i)

    def __str__(self):
        attr_dict = {}
        for name, value in self:
            attr_dict[name] = value
        return str(attr_dict)

    def update_value(self, name, config, *args, **kwargs):
        if isinstance(config, list):
            raise PkgetError("config shoule not be a list", "config")
        value = None
        if isinstance(config, dict):
            if not (name in config):
                return
            value = config[name]
        else:
            if not hasattr(config, name):
                return
            value = getattr(config, name)
        return update_value(self, name, value, *args, **kwargs)

    def update_config(self, config, override=False):
        for attr_name, attr_value in self:
            kwargs = {}
            if isinstance(attr_value, bool):
                kwargs = {"ignore_not_true": False,
                          "ignore_false": False}
            elif isinstance(attr_value, dict):
                pass
            elif isinstance(attr_value, list):
                pass
            else:
                pass
            self.update_value(attr_name, config, **kwargs)
