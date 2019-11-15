# -*- encoding: utf-8 -*-
"""
@File    : error_code.py
@Time    : 2019/11/7 15:19
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from werkzeug.exceptions import HTTPException

from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = 'sorry ,we made a mistake'
    error_code = 999


class ClientTypeError(HTTPException):
    code = 400
    msg = 'clinet is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parmeter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not_found 0_0.'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'