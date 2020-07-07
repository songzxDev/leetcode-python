# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 0027 18:46
# @Author  : songzhenxi
# @Email   : songzx_2326@163.com
# @File    : getjeektime.py
# @Software: PyCharm

import base64
import os

from Crypto.Cipher import AES

if __name__ == '__main__':
    key = '12345678901234567890123456789012'
    cryptor = AES.new(key, AES.MODE_CBC, os.urandom(16))
    cryptedstr = base64.b64decode('WPA0YdPXrBDZp3TKeDJDjuzdkT/TIKsY3c2JMfeE3PuwFSZa5gs4pe1IPwhY2yUhb5L5oMTwXGSEKQRc7YHNR7eF6VmS6V+vO9YNm3fczwdQQbY/PRR1Cc7Kj2GMInBM')
    recovery = cryptor.decrypt(cryptedstr)
    print recovery.rstrip('\0')[16:]

