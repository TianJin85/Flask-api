# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    :  2019/11/17 15:51
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""


class QiYue(object):
    name = 'qiyue'
    age = 18

    def __init__(self):
        self.gender = 'male'

    def keys(self):
        return ('name', 'age')

    def __getitem__(self, item):
        return getattr(self, item)


o = QiYue()
print(dict(o))