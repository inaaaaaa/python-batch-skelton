# -*- coding: utf-8 -*-

import logging


logger = logging.getLogger(__name__)


class ProcessBContext:
    def __init__(self, conf):
        pass


class ProcessB:
    def __init__(self, conf):
        self.ctx = ProcessBContext(conf)

    def run(self):
        logging.info('start')
        logging.info('end')
