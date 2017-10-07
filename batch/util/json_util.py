# -*- coding: utf-8 -*-

import json
import logging


logger = logging.getLogger(__name__)


class JsonUtil:
    def __init__(self):
        pass

    def parse_json(self, str_):
        if str_ is None or str_ == '':
            return {}

        return json.loads(str_)
