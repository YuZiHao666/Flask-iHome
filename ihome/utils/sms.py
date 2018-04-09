# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from ihome.libs.yuntongxun.CCPRestSDK import REST
import ConfigParser

# ���ʺ�
accountSid = '8a216da86276486901628597908606ee'

# ���ʺ�Token
accountToken = '0770d5aa88de4ea7a404e475eddc57c2'

# Ӧ��Id
appId = '8a216da8627648690162859790d706f4'

# �����ַ����ʽ���£�����Ҫдhttp://
serverIP = 'app.cloopen.com'

# ����˿�
serverPort = '8883'

# REST�汾��
softVersion = '2013-12-26'


class CCP(object):
    """�Զ��嵥���࣬���ڷ��Ͷ���"""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(CCP, cls).__new__(cls, *args, **kwargs)

            # ��ʼ��REST SDK
            cls._instance.rest = REST(serverIP, serverPort, softVersion)
            cls._instance.rest.setAccount(accountSid, accountToken)
            cls._instance.rest.setAppId(appId)

        return cls._instance

    def send_template_sms(self, to, datas, tempId):
        """�������Ͷ��ŵķ���
        ����ֵ�������1,��ʾ��ͨѶ�����Ƿ��Ͷ����ǳɹ��ģ������0����ʾʧ��
        """

        # result : ����ͨ�Ÿ��߿����ߵĽ����Ϣ
        result = self.rest.sendTemplateSMS(to, datas, tempId)

        # return�Ľ��ֵ���ǿ����߸����û������Ƿ��ͳɹ�
        if result.get('statusCode') == '000000':
            return 1
        else:
            return 0
