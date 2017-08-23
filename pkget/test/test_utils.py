import unittest
from pkget import Utils


class UtilsTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_set_value(self):
        def test_result(target, name, value):
            message = "target is "
            if isinstance(target, dict):
                self.assertIs(target[name], value, message + "dict")
            elif isinstance(target, list):
                self.assertIs(target[-1], value, message + "list")
            else:
                self.assertIs(
                    getattr(target, name), value, message + "object")

        def test_set_value_when_target(target):
            Utils.set_value(target, "a", "1")
            test_result(target, "a", "1")
            Utils.set_value(target, "b", 2)
            test_result(target, "b", 2)
            Utils.set_value(target, "a", 1)
            test_result(target, "a", 1)

            Utils.set_value(target, "a", "", ignore_not_true=True)
            test_result(target, "a", 1)
            Utils.set_value(target, "a", "", ignore_not_true=False)
            test_result(target, "a", "")
            Utils.set_value(target, "a", False, ignore_not_true=False,
                            ignore_false=True)
            test_result(target, "a", "")
            Utils.set_value(target, "a", False, ignore_not_true=False,
                            ignore_false=False)
            test_result(target, "a", False)
            Utils.set_value(target, "a", None, ignore_not_true=False,
                            ignore_none=True)
            test_result(target, "a", False)
            Utils.set_value(target, "a", None, ignore_not_true=False,
                            ignore_none=False)
            test_result(target, "a", None)

        target = TestObject()
        test_set_value_when_target(target)
        target = {}
        test_set_value_when_target(target)
        target = []
        test_set_value_when_target(target)

    def test_update_value(self):
        self.test_set_value()
        target = {"a": {"a": 1, "b": 2}}
        Utils.update_value(target, "a", {"c": 3, "a": 3}, merge_value=True)
        self.assertIs(target["a"]["c"], 3)
        self.assertIs(target["a"]["a"], 3)

        target = {"a": [1, 2, 3]}
        Utils.update_value(target, "a", [4, 5, 6], merge_value=True)
        self.assertIs(target["a"][3], 4)
        self.assertIs(target["a"][4], 5)
        self.assertIs(target["a"][5], 6)


class TestObject():
    pass
