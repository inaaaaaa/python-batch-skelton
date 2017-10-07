# -*- coding: utf-8 -*-

import logging
import os
import yaml


logger = logging.getLogger(__name__)


class YamlUtil:
    def __init__(self):
        pass

    def parse_yaml(self, conf_path):
        if conf_path is None:
            return {}

        if not os.path.exists(conf_path):
            raise('not found: {}'.format(conf_path))

        with open(conf_path) as f:
            return yaml.load(f)
