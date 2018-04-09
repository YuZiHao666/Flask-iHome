# -*- coding: utf-8 -*-
import logging
import redis


class Config(object):
    '''加载配置'''
    # 开启调试模式
    DEBUG = True

    # 配置安全秘钥：CSRF基于session的，所以需要配置安全秘钥
    SECRET_KEY = 'qwertyasdfghzxcvbnpoiuytrlkjhgfmnbvcx'

    # 配置mysql数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:210916@127.0.0.1:3306/ihome'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 配置session存储数据的redis
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 开启数据签名 让session数据不以明文形式存储
    SESSION_USE_SIGNER = True
    # 设置超时时长
    PERMANENT_SESSION_LIFETIME = 86400  # 单位是秒


class DevelopmentConfig(Config):
    '''创建调试环境下的配置类'''
    # 调试模式和配置config一致 所以pass
    LOGGIONG_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    '''创建线上环境配资类'''
    # 重写与有差异的配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:210916@127.0.0.1:3306/ihome'
    LOGGIONG_LEVEL = logging.WARN


class UnittestConfig(Config):
    '''单元测试的配置'''
    # 重写有差异性的配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:210916@127.0.0.1:3306/ihome'


configs = {
    'default_config': Config,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'unittest': UnittestConfig
}
