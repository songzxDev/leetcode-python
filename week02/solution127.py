# -*- coding: utf-8 -*-
# @Time    : 2020-01-03 08:40
# @Author  : songzhenxi
# @Email   : songzx_2326@163.com
# @File    : solution127.py
# @Software: PyCharm


# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#
#
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
#
#
# 说明:
#
#
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
#
#
# 示例 1:
#
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出: 5
#
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#     返回它的长度 5。
#
#
# 示例 2:
#
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: 0
#
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
# Related Topics 广度优先搜索
from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        treemap = defaultdict(list)
        WORDLEN = len(endWord)
        for word in wordList:
            for k in xrange(WORDLEN):
                statuskey = word[0:k] + '*' + word[k + 1:]
                treemap[statuskey].append(word)
        visited, queue = {beginWord}, [(beginWord, 1,)]
        while queue:
            curword, curlen = queue.pop(0)
            for k in xrange(WORDLEN):
                statuskey = curword[0:k] + '*' + curword[k + 1:]
                if statuskey in treemap:
                    for word in treemap[statuskey]:
                        if word == endWord:
                            return curlen + 1
                        elif word not in visited:
                            visited.add(word)
                            queue.append((word, curlen + 1,))
                    treemap[statuskey] = []
        return 0
# leetcode submit region end(Prohibit modification and deletion)
