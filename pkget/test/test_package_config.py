import unittest
from pkget import PackageConfig


class PackageConfigTest(unittest.TestCase):
    def test_update_config(self):
        pc = PackageConfig()
        print(pc)
