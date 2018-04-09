# -*- coding: utf-8 -*-
from functools import wraps

from flask import session, jsonify,g
from werkzeug.routing import BaseConverter

from ihome.utils.response_code import RET


class RegexConverter(BaseConverter):
    '''自定义路由转换器'''

    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        self.regex = args[0]


def login_required(view_func):
    """校验用户是否是登陆用户"""
    # 装饰器在装饰一个函数时,会修改函数的__name__属性
    @wraps(view_func)
    def wraaper(*args,**kwargs):
        # 获取user_id
        user_id = session.get('user_id')

        if not user_id:
            return jsonify(errno=RET.SESSIONERR, errmsg='用户未登录')
        else:
            # 表示用户已登陆,使用g变量保存性user_id 方便在view_func调用的时候  内部可以直接使用user_id
            g.user_id = user_id

            return view_func(*args,**kwargs)
    return wraaper