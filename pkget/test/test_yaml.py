import unittest
import os
from pkget import Yaml


class YamlTest(unittest.TestCase):
    def test_load_all(self):
        def test_load_all(*args, **kwargs):
            result = []
            for item in Yaml.load_all(*args, **kwargs):
                result.append(item)
            return result

        def assert_yaml_file_1(result, index=0):
            self.assertEqual(result[index]["default"]["recipepaths"], [None])
            self.assertEqual(
                result[index]["default"]["installprefix"], "~/.local")
            self.assertEqual(
                result[index]["default"]["pkginfoprefix"], "~/.local/pkgetinfo")
            self.assertEqual(
                result[index]["local"]["recipepaths"], ["/usr/local", None])
            self.assertEqual(
                result[index]["local"]["installprefix"], "/usr/local/")
            self.assertEqual(
                result[index]["local"]["pkginfoprefix"], "/usr/local/pkgetinfo")

            self.assertEqual(
                result[1 + index]["global"]["recipepaths"], None)
            self.assertEqual(
                result[1 + index]["global"]["installprefix"], "/usr/local/")
            self.assertEqual(
                result[1 + index]["global"]["pkginfoprefix"],
                "/usr/local/pkgetinfo")

        def assert_yaml_file_2(result, index=0):
            self.assertEqual(
                result[index]["etcd"]["description"],
                "Highly-available key value store for shared configuration and \
service discovery")
            self.assertEqual(
                result[index]["etcd"]["website"], "https://github.com/coreos/etcd")
            self.assertEqual(result[index]["etcd"]["type"], "tar.gz")
            self.assertEqual(result[index]["etcd"]["version"], "3.2.5")
            self.assertEqual(result[index]["etcd"]["os"], "linux")
            self.assertEqual(result[index]["etcd"]["arch"], "amd64")
            self.assertEqual(result[index]["etcd"]["url"], None)
            self.assertEqual(
                result[index]["etcd"]["urlprefix"],
                "https://github.com/coreos/etcd/releases/download")
            self.assertEqual(result[index]["etcd"]["depends"], None)

        result = test_load_all(
            filenames=os.path.join(
                os.path.dirname(__file__), "test_yaml_1.yaml"))
        assert_yaml_file_1(result)

        result = test_load_all(
            filenames=[os.path.join(
                os.path.dirname(__file__), "test_yaml_1.yaml"),
                       os.path.join(
                           os.path.dirname(__file__), "test_yaml_2.yaml")])
        assert_yaml_file_1(result)
        assert_yaml_file_2(result, 2)

        result = test_load_all(contents="--- \n\
                      a: 12 \n\
                      b: df \n")
        self.assertEqual(result[0]["a"], 12)
        self.assertEqual(result[0]["b"], "df")

        result = test_load_all(
            contents=["---\na: 23\nb: ddd\n",
                      "---\na: df\nb: 45\n---\ng: 34\n"])
        self.assertEqual(result[0]["a"], 23)
        self.assertEqual(result[0]["b"], "ddd")
        self.assertEqual(result[1]["a"], "df")
        self.assertEqual(result[1]["b"], 45)
        self.assertEqual(result[2]["g"], 34)

        result = test_load_all(
            contents=["---\na: 23\nb: ddd\n",
                      "---\na: df\nb: 45\n---\ng: 34\n"],
            filenames=[os.path.join(os.path.dirname(__file__),
                                    "test_yaml_1.yaml"),
                       os.path.join(os.path.dirname(__file__),
                                    "test_yaml_2.yaml")])
        self.assertEqual(result[0]["a"], 23)
        self.assertEqual(result[0]["b"], "ddd")
        self.assertEqual(result[1]["a"], "df")
        self.assertEqual(result[1]["b"], 45)
        self.assertEqual(result[2]["g"], 34)
        assert_yaml_file_1(result, 3)
        assert_yaml_file_2(result, 5)

