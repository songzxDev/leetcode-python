# -*- coding:utf-8 -*-
from collections import defaultdict
import xpinyin
import json
import os

sourcedata = ['我的工作台#1-0', '系统管理#2-1', '公司定义#3-2', '系统参数#4-2', '操作员档案#5-2', '单据号管理#6-2', '会计周期#7-2', '启用帐套#8-2',
              '期末加权#9-2', '余额结转#10-2', '日志#11-2', '档案管理#12-1', '商品档案#13-12', '仓库档案#14-12', '客户档案#15-12', '供应商档案#16-12',
              '往来档案#17-12', '部门档案#18-12', '员工档案#19-12', '库管档案#20-12', '银行资料#21-12', '资金账户#22-12', '费用档案#23-12',
              '仓库管理#24-1', '入库单#25-24', '销货单#26-24', '库存转移#27-24', '库存盘点#28-24', '库存期初#29-24', '统计分析#30-24',
              '库存商品总账#31-30', '库存商品明细#32-30', '存货结存明细#33-30', '入库明细#34-30', '销售明细#35-30', '库存转移明细#36-30',
              '库存盘点明细#37-30', '库存报警查询#38-30', '发票管理#39-1', '进项发票#40-39', '销项发票#41-39', '采购发票期初#42-39', '销售发票期初#43-39',
              '统计分析#44-39', '采购发票明细#45-44', '销售发票明细#46-44', '非主营收支#47-1', '非主营收入#48-47', '非主营支出#49-47', '统计分析#50-47',
              '资金管理#51-1', '收款结算#52-51', '付款结算#53-51', '账户调拨#54-51', '统计分析#55-51', '供方往来明细#56-55', '供方往来余额#57-55',
              '客户往来明细#58-55', '客户往来余额#59-55', '部门往来查询#60-55', '部门往来明细#61-60', '部门往来余额#62-60', '部门应收明细#63-60',
              '部门应收余额#64-60', '部门应付明细#65-60', '部门应付余额66#-60', '个人往来查询#67-55', '个人往来明细#68-67', '个人往来余额#69-67',
              '个人应收明细#70-67', '个人应收余额#71-67', '个人应付明细#72-67', '个人应付余额#73-67', '其它往来查询#74-55', '其它往来明细#75-74',
              '其它往来余额#76-74', '其它应收明细#77-74', '其它应收余额#78-74', '其它应付明细#79-74', '其它应付余额#80-74', '收款结算清单#81-55',
              '付款结算清单#82-55', '账户收支明细#83-55', '账户收支余额#84-55', '账户资金预估表#85-55', '往来互抵明细表#86-55', '付款分析#87-51',
              '预付明细#88-87', '预付余额#89-87', '应付余额#90-87', '收款分析#91-51', '预收明细#92-91', '预收余额#93-91', '应付余额#94-91',
              '决策分析#95-1', '销售利润表#96-95', '批次利润表#97-95', '进销存汇总表#98-95', '进销存汇总表#99-95']
if __name__ == '__main__':
    nextarray, pinyin = [], xpinyin.Pinyin()
    for data in sourcedata:
        name, ipd = data.split('#')
        iid, pid = ipd.split('-')
        name = name.decode('utf-8')
        nextarray.append({'id': iid, 'pId': pid, 'name': name, 'open': True,
                          'url': pinyin.get_pinyin(name, ''),
                          'target': '_self'
                          })

    pidset = set([na['pId'] for na in nextarray])
    leafnodes = [na for na in nextarray if na['id'] not in pidset]
    pIdCache = defaultdict(dict)
    for na in nextarray:
        pIdCache[na['id']] = na
    for lfn in leafnodes:
        find, lfnurl = pIdCache[lfn['id']], []
        while find and find['id'] != '1':
            lfnurl.append(find['url'])
            find = pIdCache[find['pId']]
        lfnurl.reverse()
        lfn['url'] = '#' + '/'.join(lfnurl)
    root = nextarray[0]

    print json.dumps(leafnodes, ensure_ascii=False)

    # def build_tree(tree, level):
    #     if not tree:
    #         return tree
    #     tree['nodeLevel'] = level
    #     tree['children'] = [dt for dt in nextarray if dt['pId'] == tree['id']]
    #     tree['isParent'] = level < 2 or len(tree['children']) > 0
    #     if tree['children']:
    #         for child in tree['children']:
    #             build_tree(child, level + 1)
    #     return tree
    #
    #
    # build_tree(root, 0)
    # print json.dumps([root], ensure_ascii=False)
    # foldername = [pinyin.get_pinyin(chd['name'], '') for chd in root['children']]
    # targetfolder = 'E:\\mydemo\\html\\firstycloud\\src\\pages'
    # for fd in foldername:
    #     makefolder = os.path.join(targetfolder, fd)
    #     if not os.path.exists(makefolder):
    #         os.mkdir(makefolder)
