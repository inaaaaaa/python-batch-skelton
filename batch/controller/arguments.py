# -*- coding: utf-8 -*-

import argparse
import json
import logging


logger = logging.getLogger(__name__)


class Arguments:
    def __init__(self):
        pass

    def parse_args(self):
        parser = argparse.ArgumentParser(
            description='Batch application skelton'
        )
        parser.add_argument('-v', '--verbose', action='store_true')
        parser.add_argument(
            '-c',
            '--conf',
            help='Path to the config file',
            required=False
        )
        parser.add_argument(
            '-p',
            '--params',
            help='Parameters given by json',
            required=False
        )
        return parser.parse_args()
