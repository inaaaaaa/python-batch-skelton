# -*- coding: utf-8 -*-

from nose.tools import ok_, eq_

from batch.util.conf_util import ConfUtil


def test_make_dict():
    default_params = {'a': 0, 'b': 0, 'c': 0}
    conf_params = {'a': 1, 'b': 1}
    arg_params = {'a': 2}
    conf = ConfUtil().make_dict(default_params, conf_params, arg_params)
    eq_(conf['a'], 2)
    eq_(conf['b'], 1)
    eq_(conf['c'], 0)
