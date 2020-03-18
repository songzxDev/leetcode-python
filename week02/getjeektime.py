# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 0027 18:46
# @Author  : songzhenxi
# @Email   : songzx_2326@163.com
# @File    : getjeektime.py
# @Software: PyCharm

from io import StringIO
import re
import requests
import os
import sys
import requests
import datetime
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import base64
if __name__ == '__main__':
    key = 'Njk2NTAzZGEtOGMxZS00NjJkLWI5NTItMGQ3M2M4MDQzMjU5OTZ5YkYvN09ZWUlsamNGMTZuVXpXNTlUeVJlVVBXeXRBQUFBQUFBQUFBQ24yR1dlN1lwTTFDQVRqM081di9Cd2FvMVRJYlMxc2IvTUFCZVRxZjBDSUpDb0pBbVUzLzJJ'
    print key
    cryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC)
    print cryptor
    # basepath = 'F:\\jeektime\\0001\\'
    # baseuri = 'https://media001.geekbang.org/f2fba89e3d934d7eb05317c1bb111a72/'
    # m3u8_uri = 'https://media001.geekbang.org/f2fba89e3d934d7eb05317c1bb111a72/4d99fa45029b4d6cbd65094e76106a23-877f6d21baf6fee2296d5acdb40ccf6f-hd-encrypt-stream.m3u8'
    # reps = requests.get(url=m3u8_uri)
    # m3u8desc = reps.text
    # findlst = re.findall(r'4d99fa45029b4d6cbd65094e76106a23.*?\.ts', m3u8desc)
    # findlst.sort()
    # for fd in findlst:
    #     res = requests.get(r'{0}{1}'.format(baseuri, fd))
    #     cryptor = AES.new(key, AES.MODE_CBC, key)
    #     with open('{0}{1}'.format(basepath, fd), 'wb+') as fp:
    #         fp.write(cryptor.decrypt(res.content))
