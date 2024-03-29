# -*- encoding: utf-8 -*-
"""
@File    : base.py
@Time    : 2019/11/12 21:08
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self,):
        data = request.json
        super(BaseForm, self).__init__(data=data)

    def validate(self):
        pass

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # form errors
            raise ParameterException(msg=self.errors)
        return self
