# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler

import redis
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
# cSrf 防护导入
from flask_wtf.csrf import CSRFProtect

from config import configs

# 创建连接mysql对象
from ihome.utils.common import RegexConverter

db = SQLAlchemy()

# 创建可以被外界导入的连接到redis数据库的对象
redis_store = None


def setupLogging(level):
    '''工厂方法,根据外界传入的不同参数,实例话不同场景的app'''

    # 设置日志的记录等级
    logging.basicConfig(level=level)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式      日志等级    输入日志信息的文件名 行数    日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


# default——config == config——name

def get_app(config_name):
    '''工厂方法：根据不同的配置信息 实例化不同的app'''

    # 调用封装日志
    setupLogging(configs[config_name].LOGGIONG_LEVEL)

    # 创建flask应用
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(configs[config_name])

    db.init_app(app)

    # 创建连接到redis数据库对象
    global redis_store
    redis_store = redis.StrictRedis(host=configs[config_name].REDIS_HOST, port=configs[config_name].REDIS_PORT)

    # 开启cSrf保护
    CSRFProtect(app)

    # 使用session扩展,将session数据存储到redis
    Session(app)

    # 注册路由转换器
    app.url_map.converters['re'] = RegexConverter

    # 为了解决导入api时 还没有redis——store造成的 ImportError： cannot import name redis——store
    from ihome.api_1_0 import api
    # 注册蓝图
    app.register_blueprint(api)
    # 注册蓝图
    from ihome.web_html import html_blue
    app.register_blueprint(html_blue)

    return app
