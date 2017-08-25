from .exception import PkgetError
from .utils import Utils


class BasicConfig():
    __type = {"int": "int",
              "float": "float",
              "string": "string",
              "dict": "dict",
              "list": "list"}

    def __init__(self, attributes):
        self.__attributes = {}
        if isinstance(attributes, dict):
            for i in attributes:
                if isinstance(attributes[i], dict):
                    self.__attributes[i] = attributes[i]
                else:
                    self.__attributes[i] = {"value": attributes[i]}
        elif isinstance(attributes, list):
            for i in attributes:
                self.__attributes[i] = {}

        for i in self.__attributes:
            if not ("value" in self.__attributes[i]):
                self.__attributes[i]["value"] = ""

            if "type" in self.__attributes[i]:
                self.__attributes[i]["type"] = self.__detect_attribute_type(
                    type_name=self.__attributes[i]["type"])
            else:
                self.__attributes[i]["type"] = self.__detect_attribute_type(
                    attr_value=self.__attributes[i]["value"])

    def __iter__(self):
        for i in self.__attributes:
            yield i, getattr(self, i)

    def __str__(self):
        attr_dict = {}
        for name, value in self:
            attr_dict[name] = value
        return str(attr_dict)

    def __getattribute__(self, name):
        return super().__getattribute__(name)

    def __getattr__(self, name):
        if hasattr(self, "__attributes") and \
                (name in self.__attributes):
            return self.__attributes[name]["value"]
        raise PkgetError("attribute %s is not found" % name,
                         "config")

    def __setattr__(self, name, value):
        attr_type = self.__detect_attribute_type(attr_value=value)
        if attr_type != self.__attributes[name]["type"]:
            raise PkgetError(
                "type of %s is not %s" %
                (name, self.__attributes[name]["type"]),
                "config")
        return super().__setattr__(name, value)

    def __detect_attribute_type(self, attr_value="", type_name=""):
        attr_type = "unknown"
        if not attr_type:
            attr_type = type_name
        elif isinstance(attr_value, int):
            attr_type = "int"
        elif isinstance(attr_value, float):
            attr_type = "float"
        elif isinstance(attr_value, dict):
            attr_type = "dict"
        elif isinstance(attr_value, list):
            attr_type = "list"
        elif isinstance(attr_value, str):
            attr_type = "string"

        if attr_type in self.__type:
            return self.__type[attr_type]
        raise PkgetError("%s type is not allowed" % attr_type, "config")

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

        return Utils.update_value(self, name, value, *args, **kwargs)

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
