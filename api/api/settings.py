# -*- coding: utf8 -*-
import os
import importlib

env = os.environ.get("woxenv","prod")
print("current env => {}".format(env))

if env == "dev":
    from api.setting.dev import *
elif env == "prod":
    from api.setting.prod import *
elif env == "test":
    from api.setting.test import *