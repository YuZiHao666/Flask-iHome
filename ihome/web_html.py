# -*- coding: utf-8 -*-
from flask import Blueprint, current_app, make_response
from flask_wtf.csrf import generate_csrf

html_blue = Blueprint('html_blue', __name__)


@html_blue.route('/<re(".*"):file_name>')
def get_static_html(file_name):
    '''获取静态文件'''
    # 需求1：127.0.0.1:5000/login.html
    # 加载ico图标
    if not file_name:
        file_name = 'index.html'

    if file_name != 'favicon.ico':
        # 拼接file——name所在的路径 'static/html/file_name'
        file_name = 'html/' + file_name



    # 获取response
    response = make_response(current_app.send_static_file(file_name))
    token = generate_csrf()
    # 将csrf_token数据写入到cookie
    response.set_cookie('csrf_token', token)
    # 使用file_path去查找指定路径下的静态html
    return response