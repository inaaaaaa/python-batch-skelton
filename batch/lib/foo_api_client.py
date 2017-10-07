# -*- coding: utf-8 -*-

import logging


logger = logging.getLogger(__name__)


class FooApiClient:
    def __init__(self, url):
        self.url = url

    def get(self):
        return {'aaa': 'foo'}
