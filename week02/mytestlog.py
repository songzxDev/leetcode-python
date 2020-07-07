# -*- coding: utf-8 -*-
# @Time    : 2020-05-27 20:15
# @Author  : songzhenxi
# @Email   : songzx_2326@163.com
# @File    : mytestlog.py
# @Software: PyCharm
from collections import defaultdict
import requests
import time

if __name__ == '__main__':
    # mycount = defaultdict(int)
    # with open(r"G:\mygolandlog\myrunlog2.log", 'r') as fp:
    #     for line in fp.readlines():
    #         mycount[line.strip().split("atomic.")[-1]] += 1
    # print "key的总数：%d" % len(mycount.keys())
    # print "平均调用列表：%s" % str(set(mycount.values()))
    def getreport():
        while True:
            resp = requests.get('http://127.0.0.1:8089/stats/requests')
            print resp.json()['rycerz_other']
            time.sleep(3)


    getreport()
