# -*- encoding: utf-8 -*-
"""
@File    : error_code.py
@Time    : 2019/11/7 15:19
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from werkzeug.exceptions import HTTPException


class ClientTypeError(HTTPException):
    code = 400
    msg = 'clinet is invalid'
    error_code = 1006
