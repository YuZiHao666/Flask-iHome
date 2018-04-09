# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from ihome.libs.yuntongxun.CCPRestSDK import REST
import ConfigParser

# 主帐号
accountSid = '8a216da86276486901628597908606ee'

# 主帐号Token
accountToken = '0770d5aa88de4ea7a404e475eddc57c2'

# 应用Id
appId = '8a216da8627648690162859790d706f4'

# 请求地址，格式如下，不需要写http://
serverIP = 'app.cloopen.com'

# 请求端口
serverPort = '8883'

# REST版本号
softVersion = '2013-12-26'


class CCP(object):
    """自定义单例类，用于发送短信"""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(CCP, cls).__new__(cls, *args, **kwargs)

            # 初始化REST SDK
            cls._instance.rest = REST(serverIP, serverPort, softVersion)
            cls._instance.rest.setAccount(accountSid, accountToken)
            cls._instance.rest.setAppId(appId)

        return cls._instance

    def send_template_sms(self, to, datas, tempId):
        """真正发送短信的方法
        返回值：如果是1,表示云通讯向我们发送短信是成功的，如果是0，表示失败
        """

        # result : 是云通信告诉开发者的结果信息
        result = self.rest.sendTemplateSMS(to, datas, tempId)

        # return的结果值，是开发者告诉用户短信是否发送成功
        if result.get('statusCode') == '000000':
            return 1
        else:
            return 0
