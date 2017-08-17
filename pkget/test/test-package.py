#!/usr/bin/env python
from pkget import Package
import os

package = Package(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../recipes/etcd.yaml")),
    type="yaml")

print(package)
