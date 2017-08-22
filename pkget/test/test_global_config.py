import unittest
from pkget import GlobalConfig


class GlobalConfigTest(unittest.TestCase):
    def test_update_config(self):
        config = GlobalConfig()
        print("default")
        print(config)
        config.update_config({
            "installprefix": "~/.local",
            "pkginfoprefix": "~",
            "recipepaths": ["~/.local", "", None],
        })
        print(config)
        config.update_config({
            "installprefix": None,
        })
        print(config)
