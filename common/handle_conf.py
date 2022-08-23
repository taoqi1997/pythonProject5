import os
from configparser import ConfigParser
from common.Handle_path import CONFIG


class Handle_config(ConfigParser):
    def __init__(self,conf_name):
        super(Handle_config, self).__init__()
        self.read(filenames=conf_name,encoding="utf-8")
conf = Handle_config(os.path.join(CONFIG,"conf.ini"))

# if __name__ == '__main__':
#     a = conf.get("URL","url")
#     print(a)