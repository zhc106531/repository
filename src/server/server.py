from flask import Flask, jsonify, request
from flask_cors import CORS
from faker import Faker
from faker.providers import BaseProvider
import json
import requests

app = Flask(__name__)
CORS(app)  # 允许所有域的跨域请求
dev="worktest5"
def generate_random_name_and_phone(name=None, phone_number=None, account=None, password='123456aA'):
    """
    返回账号信息
    :return: name, phone_number, account
    """
    faker = Faker(locale='zh-CN')

    def provider_random_number(self, length):
        return self.random_int(10 ** (length - 1), 10 ** length - 1)

    if name is None:
        name = faker.name()

    if phone_number is None:
        phone_number = faker.phone_number()

    BaseProvider.random_number = provider_random_number
    fake = Faker()
    if account is None:
        account = 'cc' + str(fake.random_number(length=7))

    return name, phone_number, account, password

def checkVvId(vvid: str):
    url = f"https://{dev}.vvtechnology.cn/api/user/public/pc/v1/account/checkVvId"
    payload = json.dumps({
        "vvId": vvid
    })
    headers = {
        'authorization': '',
        'x-device-model': 'windows',
        'x-device-name': '%E6%B5%8B%E8%AF%95-%E8%B5%B5%E6%83%A0%E6%88%90',
        'x-device-no': 'AC6D6206-BD6F-4949-8895-32132A059ADB',
        'x-device-version': 'Windows 10 Home China',
        'uc': '',
        'vv-client-version': '1.7.25',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'content-type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.json()['data'] is False:
        return True
    else:
        return False
def checkPhone(phone: str):
    url = f"https://{dev}.vvtechnology.cn/api/user/public/v3/account/sendVerificationCode"

    payload = json.dumps({
        "type": 5,
        "loginName": phone,
        "internationalCode": "86"
    })
    headers = {
        'authorization': '',
        'x-device-model': 'windows',
        'x-device-name': '%E6%B5%8B%E8%AF%95-%E8%B5%B5%E6%83%A0%E6%88%90',
        'x-device-no': 'AC6D6206-BD6F-4949-8895-32132A059ADB',
        'x-device-version': 'Windows 10 Home China',
        'uc': '',
        'vv-client-version': '1.7.25',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'content-type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    state = True if response.json()['msg'] in ('Send a success', '发送成功', 'Send successfully') else False
    return state
def verificationcode(phone: str):
    """获取验证码"""
    url = f"https://{dev}.vvtechnology.cn/api/user/public/v3/account/sendVerificationCode"

    payload = json.dumps({
        "type": 5,
        "loginName": phone,
        "internationalCode": "86"
    })
    headers = {
        'authorization': '',
        'x-device-model': 'windows',
        'x-device-name': '%E6%B5%8B%E8%AF%95-%E8%B5%B5%E6%83%A0%E6%88%90',
        'x-device-no': 'AC6D6206-BD6F-4949-8895-32132A059ADB',
        'x-device-version': 'Windows 10 Home China',
        'uc': '',
        'vv-client-version': '1.7.25',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'content-type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()['data']['value']
def rename(nickName, userCode, authCode):
    url = f"https://{dev}.vvtechnology.cn/api/user/public/pc/v1/update"

    payload = json.dumps({
        "nickName": nickName,
        "name": nickName,
        "userCode": userCode,
        "authCode": authCode,
        "avatarFile": [
            {
                "categoryCode": "avatarFile",
                "keyNameAndOpt": [
                    "ADD:avatar_general_square_default.png"
                ]
            }
        ]
    })
    headers = {
        'authorization': '',
        'x-device-model': 'windows',
        'x-device-name': '%E6%B5%8B%E8%AF%95-%E8%B5%B5%E6%83%A0%E6%88%90',
        'x-device-no': 'AC6D6206-BD6F-4949-8895-32132A059ADB',
        'x-device-version': 'Windows 10 Home China',
        'uc': '',
        'vv-client-version': '1.7.25',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'content-type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    state = True if response.json()['msg'] == '操作成功' else False
    return state

def register_vv(vvid, password, mobile, verificationValue):
    url = f"https://{dev}.vvtechnology.cn/api/user/public/pc/v4/account/register"

    payload = json.dumps({
        "loginName": vvid,
        "password": password,
        "countryCode": "39",
        "internationalCode": "86",
        "mobile": mobile,
        "verificationValue": verificationValue,
        "clientId": "1470305119391260673",
        "addLoginDevice": 0
    })
    headers = {
        'authorization': '',
        'x-device-model': 'windows',
        'x-device-name': '%E6%B5%8B%E8%AF%95-%E8%B5%B5%E6%83%A0%E6%88%90',
        'x-device-no': 'AC6D6206-BD6F-4949-8895-32132A059ADB',
        'x-device-version': 'Windows 10 Home China',
        'uc': '',
        'vv-client-version': '1.7.25',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'content-type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    userCode = response.json()['data']['userCode']
    authCode = response.json()['data']['authCode']

    return userCode, authCode

def zc(num=1):
    """
    注册用户
    :param num: 注册人数
    :return:
    """
    for i in range(num):
        name, phone, account, password = generate_random_name_and_phone()
        if checkVvId(account) is True and checkPhone(phone) is True:
            verification_number = verificationcode(phone)
            userCode, authCode = register_vv(account, password, phone, verification_number)
            rename(name, userCode, authCode)
            print(name, phone, account, password)
            return name, phone, account, password

@app.route('/api/register', methods=['GET'])
def register():
    num = int(request.args.get('num', 1))  # 默认生成一个账号信息
    accounts = []

    for _ in range(num):
        # name, phone, account, password = generate_random_name_and_phone()
        name, phone, account, password = zc()

        accounts.append({'name': name, 'phone': phone, 'account': account, 'password': password})

    return jsonify({'message': '成功','accounts': accounts})

if __name__ == '__main__':
    app.run(debug=True)
