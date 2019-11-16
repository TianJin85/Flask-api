# -*- encoding: utf-8 -*-
"""
@File    : token_auth.py
@Time    : 2019/11/6 13:49
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


def verify_password(account, password):
    # token
    return True