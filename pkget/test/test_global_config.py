import unittest
import os
from pkget import GlobalConfig, Utils


class GlobalConfigTest(unittest.TestCase):
    def test_update_config(self):
        config = GlobalConfig()
        recipepaths = \
            [os.path.join(
                os.path.dirname(os.path.dirname(__file__)),  "recipes")]
        self.assertEqual(config.recipepaths, recipepaths)
        self.assertIs(config.installprefix, "")
        self.assertIs(config.pkginfoprefix, "")
        config.update_config({
            "installprefix": "~/.local",
            "pkginfoprefix": "~",
            "recipepaths": ["~/.local", "", None],
        })
        recipepaths.append(Utils.abspath("~/.local"))

        self.assertEqual(config.recipepaths, recipepaths)
        self.assertEqual(config.installprefix, Utils.abspath("~/.local"))
        self.assertEqual(config.pkginfoprefix, Utils.abspath("~"))

        config.update_config({
            "installprefix": "",
            "pkginfoprefix": None,
            "recipepaths": ["", None],
        })
        self.assertEqual(config.recipepaths, recipepaths)
        self.assertEqual(config.installprefix, Utils.abspath("~/.local"))
        self.assertEqual(config.pkginfoprefix, Utils.abspath("~"))
