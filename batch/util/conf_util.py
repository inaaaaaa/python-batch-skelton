# -*- coding: utf-8 -*-

import logging


logger = logging.getLogger(__name__)


class ConfUtil:
    def __init__(self):
        pass

    def make_dict(
        self,
        default_params,
        conf_params,
        arg_params
    ):
        ret = {}
        self._set_params(ret, default_params)
        self._set_params(ret, conf_params)
        self._set_params(ret, arg_params)
        return ret

    def _set_params(self, dict_, params):
        if params is None:
            return

        for k, v in params.items():
            dict_[k] = v
