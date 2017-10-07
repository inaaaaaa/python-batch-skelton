# -*- coding: utf-8 -*-

import logging

from batch.lib.foo_api_client import FooApiClient


logger = logging.getLogger(__name__)


class ProcessAContext:
    def __init__(self, conf):
        self._url = conf['url']
        self._param_a = conf['param_a']

    @property
    def url(self):
        return self._url

    @property
    def param_a(self):
        return self._param_a


class ProcessA:
    def __init__(self, conf):
        self.ctx = ProcessAContext(conf)
        self.foo_api_client = FooApiClient(self.ctx.url)

    def run(self):
        logger.info('start')

        res = self.foo_api_client.get()
        if res['aaa'] != self.ctx.param_a:
            raise RuntimeError('bar')

        logger.info('end')
