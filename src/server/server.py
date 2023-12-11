from flask import Flask, jsonify, request
from flask_cors import CORS
from faker import Faker
from faker.providers import BaseProvider

app = Flask(__name__)
CORS(app)  # 允许所有域的跨域请求

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
        account = 'vv' + str(fake.random_number(length=7))

    return name, phone_number, account, password

@app.route('/api/register', methods=['GET'])
def register():
    num = int(request.args.get('num', 1))  # 默认生成一个账号信息
    accounts = []

    for _ in range(num):
        name, phone, account, password = generate_random_name_and_phone()
        accounts.append({'name': name, 'phone': phone, 'account': account, 'password': password})

    return jsonify({'message': '成功','accounts': accounts})

if __name__ == '__main__':
    app.run(debug=True)
