from .exception import PkgetError
from .utils import update_value


class BasicConfig():
    def __init__(self, attributes):
        self.attributes = {}
        if isinstance(attributes, dict):
            for i in attributes:
                if isinstance(attributes[i], dict):
                    self.attributes[i] = attributes[i]
                else:
                    self.attributes[i] = {"default": attributes[i]}
        elif isinstance(attributes, list):
            for i in attributes:
                self.attributes[i] = {}

        for i in self.attributes:
            if not ("default" in self.attributes[i]):
                self.attributes[i]["default"] = ""
            setattr(self, i, self.attributes[i]["default"])

    def __str__(self):
        print_dict = {}
        for i in self.attributes:
            print_dict[i] = getattr(self, i)
        return str(print_dict)

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
        for i in self.attributes:
            attr = getattr(self, i)
            kwargs = {}
            if isinstance(attr, bool):
                kwargs = {"ignore_not_true": False,
                          "ignore_false": False}
            elif isinstance(attr, dict):
                pass
            elif isinstance(attr, list):
                pass
            else:
                pass
            self.update_value(i, config, **kwargs)
