#!/usr/bin/env python
import os
from pkget import ConfigManager

cm = ConfigManager()

contents = cm.load_yaml(
    os.path.join(os.path.dirname(__file__), "../config/pkget.yaml"))
print(contents)
