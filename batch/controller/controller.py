# -*- coding: utf-8 -*-

import json
import logging
import os
import yaml

from batch.controller.arguments import Arguments
from batch.process.process_a import ProcessA
from batch.process.process_b import ProcessB
from batch.util.conf_util import ConfUtil
from batch.util.json_util import JsonUtil
from batch.util.yaml_util import YamlUtil


logger = logging.getLogger(__name__)


default_params = {
    'process': 'process_a',
    'param_a': 'param_a',
    'param_b': 'param_b',
    'param_c': 'param_c',
    'url': '/foo/foo'
}


class Controller:
    def __init__(self, args):
        conf_path, arg_params_json = args.conf, args.params
        conf_params = YamlUtil().parse_yaml(conf_path)
        arg_params = JsonUtil().parse_json(arg_params_json)
        self.conf = ConfUtil().make_dict(default_params, conf_params, arg_params)

    def run(self):
        if self.conf['process'] == 'process_a':
            ProcessA(self.conf).run()
        elif self.conf['process'] == 'process_b':
            ProcessB(self.conf).run()
        else:
            raise RuntimeError('invalid process')
