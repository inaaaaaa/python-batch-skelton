#!/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import logging.config
import os
import sys
import traceback

from batch.controller.arguments import Arguments
from batch.controller.controller import Controller


logger = logging.getLogger(__file__)


def setup_logging(
    default_path='conf/simple_logging.json',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=level)


if __name__ == '__main__':
    args = Arguments().parse_args()

    setup_logging()

    if sys.version_info.major != 3:
        logger.error('please use python3')
        sys.exit(1)

    logger.info('start')
    try:
        Controller(args).run()
    except Exception as e:
        logger.error('failed: {}'.format(str(e)))
        if args.verbose:
            traceback.print_exc()
        sys.exit(1)
    else:
        logger.info('succeed')
        sys.exit(0)
