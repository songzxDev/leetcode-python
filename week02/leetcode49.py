# -*- coding: utf-8 -*-
# @Time    : 2020-05-13 17:47
# @Author  : songzhenxi
# @Email   : songzx_2326@163.com
# @File    : leetcode49.py
# @Software: PyCharm

# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
#  示例:
#
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
#  说明：
#
#
#  所有输入均为小写字母。
#  不考虑答案输出的顺序。
#
#  Related Topics 哈希表 字符串

from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def __init__(self):
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

    def getnumkey(self, stt):
        numkey = 1
        for s in stt:
            numkey *= self.primes[ord(s) - 97]
        return numkey

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mycout = defaultdict(list)
        for stt in strs:
            mycout[self.getnumkey(stt)].append(stt)
        return mycout.values()
# leetcode submit region end(Prohibit modification and deletion)
