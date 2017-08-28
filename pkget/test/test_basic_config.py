import unittest
from pkget import BasicConfig, PkgetError


class BasicConfigTest(unittest.TestCase):
    def setUp(self):
        self.basic_config = BasicConfig(
            attributes={"installprefix": None,
                        "pkginfoprefix": "",
                        "recipepaths": [],
                        "configfiles": ["~/.local"],
                        "globally": False,
                        "install": True,
                        "uninstall": {"value": False},
                        "dict_attr": {"value": {}},
                        "sub_attr": {}})

    def test_getattr(self):
        self.assertEqual(self.basic_config.installprefix, None)
        self.assertEqual(self.basic_config.pkginfoprefix, "")
        self.assertEqual(self.basic_config.recipepaths, [])
        self.assertEqual(self.basic_config.configfiles, ["~/.local"])
        self.assertEqual(self.basic_config.globally, False)
        self.assertEqual(self.basic_config.install, True)
        self.assertEqual(self.basic_config.uninstall, False)
        self.assertEqual(self.basic_config.dict_attr, {})
        self.assertEqual(self.basic_config.sub_attr, None)

    def test_setattr(self):
        with self.assertRaises(PkgetError):
            self.basic_config.installprefix = True
            self.basic_config.recipepaths = {}
        self.basic_config.installprefix = "~/.local"
        self.assertEqual(self.basic_config.installprefix, "~/.local")
        self.basic_config.pkginfoprefix = "/usr/local"
        self.assertEqual(self.basic_config.pkginfoprefix, "/usr/local")
        self.basic_config.recipepaths.append("/usr/local")
        self.assertEqual(self.basic_config.recipepaths, ["/usr/local"])
        self.basic_config.configfiles = ["/usr/local"]
        self.assertEqual(self.basic_config.configfiles, ["/usr/local"])
        self.basic_config.globally = True
        self.assertEqual(self.basic_config.globally, True)
        self.basic_config.install = False
        self.assertEqual(self.basic_config.install, False)
        self.basic_config.uninstall = True
        self.assertEqual(self.basic_config.uninstall, True)
        self.basic_config.dict_attr["a"] = 1
        self.assertEqual(self.basic_config.dict_attr, {"a": 1})
        self.basic_config.dict_attr = {"b": 2}
        self.assertEqual(self.basic_config.dict_attr, {"b": 2})
        self.basic_config.sub_attr = "test"
        self.assertEqual(self.basic_config.sub_attr, "test")

    def test_update_value(self):
        with self.assertRaises(PkgetError):
            self.basic_config.update_value("install", ["usr", "local"])
            self.basic_config.update_value(
                "test_not_exists", {"test_not_exists": True})

        self.basic_config.update_value(
            "installprefix", {"installprefix": "~/.local"})
        self.assertEqual(self.basic_config.installprefix, "~/.local")
        self.basic_config.update_value(
            "configfiles", {"configfiles": ["/usr/local"]})
        self.assertEqual(
            self.basic_config.configfiles, ["~/.local", "/usr/local"])
        self.basic_config.update_value(
            "configfiles", {"configfiles": ["/usr/local"]}, merge_value=False)
        self.assertEqual(
            self.basic_config.configfiles, ["/usr/local"])
        self.basic_config.update_value("globally", {"globally": False})
        self.assertEqual(self.basic_config.globally, False)

    def test_update_config(self):
        self.basic_config.update_config(
            config={"installprefix": "~/",
                    "pkginfoprefix": "~",
                    "recipepaths": ["~/"],
                    "globally": False,
                    "configfiles": ["~/"],
                    "dict_attr": {"a": 1}}, merge_value=False)
        self.assertEqual(self.basic_config.installprefix, "~/")
        self.assertEqual(self.basic_config.pkginfoprefix, "~")
        self.assertEqual(self.basic_config.recipepaths, ["~/"])
        self.assertEqual(self.basic_config.globally, False)
        self.assertEqual(self.basic_config.configfiles, ["~/"])
        self.assertEqual(self.basic_config.dict_attr, {"a": 1})

        self.basic_config.update_config(
            config={"installprefix": "~/local",
                    "pkginfoprefix": "~/local",
                    "recipepaths": ["/usr", "/usr/bin"],
                    "globally": True,
                    "configfiles": ["~/", "~/abc"],
                    "dict_attr": {"b": 2}}, merge_value=True)
        self.assertEqual(self.basic_config.installprefix, "~/local")
        self.assertEqual(self.basic_config.pkginfoprefix, "~/local")
        self.assertEqual(
            self.basic_config.recipepaths, ["~/", "/usr", "/usr/bin"])
        self.assertEqual(self.basic_config.globally, True)
        self.assertEqual(self.basic_config.configfiles, ["~/", "~/", "~/abc"])
        self.assertEqual(self.basic_config.dict_attr, {"a": 1, "b": 2})
