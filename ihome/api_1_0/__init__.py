# -*- coding: utf-8 -*-
from flask import Blueprint

# 一个接口版本里面需要有一个蓝图 并指定唯一版本
api = Blueprint('api_1_0', __name__, url_prefix='/api/1.0')

# 为了让api导入蓝图时 蓝图注册代码可以跟着被导入
# name视图和路由对应关系中就会有路由
from . import verify, passport, profile,house,order
