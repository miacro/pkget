import unittest
from pkget import PackageManager


class PackageManagerTest(unittest.TestCase):
    def test_update_config(self):
        pm = PackageManager()
