# flask-leancloud-sms

## 安装

```python
pip install flask-leancloud-sms
```

## 配置

| 配置项 | 说明 |
|:--------------------:|:---------------------------:|
| LEANCLOUD_APP_ID | 应用id |
| LEANCLOUD_APP_KEY | 应用key |

## 基本使用

```python
from flask import Flask
from flask_leancloud_sms import Leancloud_Sms
app = Flask(__name__)
lsms= Leancloud_Sms(app)
```

## 发送短信验证码

```python
@app.route('/send-sms/<phone>')
def send_sms(phone):
    return lsms.send_message(phone)
```

## 发送语音验证码

```python
@app.route('/send-sms/<phone>')
def send_sms(phone):
    return lsms.send_message(phone,smsType='voice')
```

## 国际短信

```python
@app.route('/send-sms/<phone>')
def send_sms(phone):
    return lsms.send_message(phone,countryCode='CN')
```

> `countryCode` 参考 [https://blog.leancloud.cn/4818/](`https://blog.leancloud.cn/4818/`)

## 自定义短信模板

```python
@app.route('/send-sms/<phone>')
def send_sms(phone):
    return lsms.send_message(phone,template='template_test',name=username,time='2017-5-1')
```

## 验证码验证

```python
@app.route('/verify-sms/<phone>/<code>')
def verify(phone,code):
    return lsms.verify_sms(phone,code)
```

## 函数返回值

- `send_message` return `true` or `false`
- `verify_sms` return `true` or `false`