import unittest
import os
from pkget import Yaml


class YamlTest(unittest.TestCase):
    def test_load_all(self):
        def test_load_all(*args, **kwargs):
            generator = Yaml.load_all(*args, **kwargs)
            for i in generator:
                print(i)

        print("\n\ntest filenames is str")
        test_load_all(
            filenames=os.path.join(os.path.dirname(__file__), "../config/pkget.yaml"))

        print("\n\ntest filenames is list")
        test_load_all(
            filenames=[os.path.join(os.path.dirname(__file__), "../config/pkget.yaml"),
                       os.path.join(os.path.dirname(__file__), "../recipes/etcd.yaml")])

        print("\n\n test contents is str")
        test_load_all(contents="--- \n\
                      a: 12 \n\
                      b: df \n")

        print("\n\n test contents is list")
        test_load_all(
            contents=["---\na: 23\nb: ddd\n", "---\na: df\nb: 45\n---\ng: 34\n"])

        print("\n\n test all")
        test_load_all(
            contents=["---\na: 23\nb: ddd\n", "---\na: df\nb: 45\n---\ng: 34\n"],
            filenames=[os.path.join(os.path.dirname(__file__), "../config/pkget.yaml"),
                       os.path.join(os.path.dirname(__file__), "../recipes/etcd.yaml")])
