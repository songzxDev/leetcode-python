# -*- coding:utf-8 -*-
from collections import defaultdict

if __name__ == '__main__':
    mymap = defaultdict(int)
    with open("D:\\mygolanglog\\myrunlog2.log", 'r') as fp:
        for line in fp.readlines():
            mymap[line.strip().split("atomic.")[-1]] += 1
    myset = set(mymap.values())
    print len(mymap.keys())
    print str(myset)
