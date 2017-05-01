# -*- coding: utf-8 -*-
import requests
class Leancloud_Sms(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
    def init_app(self,app):
        self._app_id = app.config.get('LEANCLOUD_APP_ID', '')
        self._app_key = app.config.get('LEANCLOUD_APP_KEY', '')
        self._request_sms_code_url = app.config.get('REQUEST_SMS_CODE_URL', 'https://api.leancloud.cn/1.1/requestSmsCode')
        self._verify_sms_code_url = app.config.get('VERIFY_SMS_CODE_URL', 'https://api.leancloud.cn/1.1/verifySmsCode/')
        self._send_sms_type = app.config.get('SEND_SMS_TYPE', 'sms')
        
        self._headers = {
            "X-LC-Id": 'self._app_id',
            "X-LC-Key": 'self._app_key',
            "Content-Type": "application/json",
        }
    def send_message(phone,smsType='sms',countryCode='CN',template=None,**argv):
        """
        通过 POST 请求 requestSmsCode API 发送验证码到指定手机
        :param phone: 通过网页表单获取的电话号
        :return: 
        """
        data = {
            "mobilePhoneNumber": phone,
            "smsType":sms_type,
            "countryCode":country_code,
        }
        if template is not None:
            data['template']=template,
            data=dict(data,argv)
        
        # post 方法参数包含三部分，如我们之前分析 API 所述
        # REQUEST_SMS_CODE_URL: 请求的 URL
        # data: 请求的内容，另外要将内容编码成 JSON 格式
        # headers: 请求的头部，包含 Id 与 Key 等信息
        r = requests.post(self._request_sms_code_url, data=json.dumps(data), headers=self._headers)
        # 响应 r 的 status_code 值为 200 说明响应成功
        # 否则失败
        if r.status_code == 200:
            return True
        else:
            return False
    def verify_sms(phone, code):
        """
        发送 POST 请求到 verifySmsCode API 获取校验结果
        :param phone: 通过网页表单获取的电话号
        :param code: 通过网页表单获取的验证码
        :return: 
        """
        # 使用传进的参数 code 与 phone 拼接出完整的 URL
        target_url = self._verify_sms_code_url + "%s?mobilePhoneNumber=%s" % (code, phone)
        # 这里的 POST 方法只传入了两个参数
        # target_url： 请求的 URL
        # headers: 请求的头部，包含 Id 与 Key 等信息
        r = requests.post(target_url, headers=self._headers)
        # 响应 r 的 status_code 值为 200 说明验证成功
        # 否则失败
        if r.status_code == 200:
            return True
        else:
            return False
        