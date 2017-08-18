#!/usr/bin/env python
import os
from pkget import Utils


class Config():
    def __init__(self):
        self.installprefix = ""

    def __str__(self):
        return str({"installprefix": self.installprefix})


def test_update_value(target, name):
    print("====test update_value")
    print("==test ignore_none")
    Utils.update_value(target, name, "~/.local", merge_value=False)
    print(target)
    Utils.update_value(target, name, None, merge_value=False,
                 ignore_not_true=False, ignore_false=False, ignore_none=True)
    print(target)
    Utils.update_value(target, name, None, merge_value=False,
                 ignore_not_true=False, ignore_false=False, ignore_none=False)
    print(target)

    print("==test ignore_false")
    Utils.update_value(target, name, "~/.local", merge_value=False,
                 ignore_not_true=False, ignore_false=False, ignore_none=True)
    print(target)
    Utils.update_value(target, name, False, merge_value=False,
                 ignore_not_true=False, ignore_false=True, ignore_none=True)
    print(target)
    Utils.update_value(target, name, False, merge_value=False,
                 ignore_not_true=False, ignore_false=False, ignore_none=True)
    print(target)

    print("==test ignore_not_true")
    Utils.update_value(target, name, "~/.local", merge_value=False,
                 ignore_not_true=False, ignore_false=False, ignore_none=True)
    print(target)
    Utils.update_value(target, name, "", merge_value=False,
                 ignore_not_true=True, ignore_false=False, ignore_none=True)
    print(target)
    Utils.update_value(target, name, "", merge_value=False,
                 ignore_not_true=False, ignore_false=False, ignore_none=True)
    print(target)

    print("\n====test_merge_value")
    print("==test merge dict")
    Utils.update_value(target, name, "", ignore_not_true=False, merge_value=False)
    print(target)
    Utils.update_value(target, name, {"a": 1, "b": 2}, merge_value=False)
    print(target)
    Utils.update_value(target, name, "", ignore_not_true=False, merge_value=False)
    print(target)
    Utils.update_value(target, name, {"a": 1, "b": 2}, merge_value=True)
    print(target)
    Utils.update_value(target, name, {"a": 3, "c": 3}, merge_value=True)
    print(target)
    Utils.update_value(target, name, {"a": 4, "d": 5}, merge_value=False)
    print(target)

    print("==test merge list")
    Utils.update_value(target, name, "", ignore_not_true=False, merge_value=False)
    print(target)
    Utils.update_value(target, name, [1, 3, 4], merge_value=False)
    print(target)
    Utils.update_value(target, name, "", ignore_not_true=False, merge_value=False)
    print(target)
    Utils.update_value(target, name, [1, 3, 4], merge_value=True)
    print(target)
    Utils.update_value(target, name, [2, 3, 4], merge_value=True)
    print(target)
    Utils.update_value(target, name, [3, 4, 5], merge_value=False)
    print(target)


print("\n\n======test object")
config = Config()
test_update_value(config, "installprefix")

print("\n\n======test dict")
config = {"installprefix": ""}
test_update_value(config, "installprefix")

print("\n\n======test list")
config = [""]
test_update_value(config, "installprefix")
