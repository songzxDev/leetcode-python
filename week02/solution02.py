# -*- coding: utf-8 -*-
# @Time    : 2019-11-25 10:06
# @Author  : songzhenxi
# @Email   : songzx_2326@163.com
# @File    : solution02.py
# @Software: PyCharm


class Solution(object):
    # 给定一个字符串列表，每个字符串可以是以下四种类型之一：
    # 1.整数（一轮的得分）：直接表示您在本轮中获得的积分数。
    # 2. "+"（一轮的得分）：表示本轮获得的得分是前两轮有效 回合得分的总和。
    # 3. "D"（一轮的得分）：表示本轮获得的得分是前一轮有效 回合得分的两倍。
    # 4. "C"（一个操作，这不是一个回合的分数）：表示您获得的最后一个有效 回合的分数是无效的，应该被移除。
    def calPoints(self, ops):
        """
        题目：682.棒球比赛
        标签：栈
        :type ops: List[str]
        :rtype: int
        """
        stack, sums = [], 0
        for op in ops:
            if 'C' != op and 'D' != op and '+' != op:
                stack.append(int(op))
                sums += stack[-1]
            elif len(stack) > 0 and 'C' == op:
                sums -= stack.pop()
            elif len(stack) > 0 and 'D' == op:
                stack.append(stack[-1] * 2)
                sums += stack[-1]
            elif len(stack) > 0 and '+' == op:
                stack.append(stack[-1] + stack[-2] if len(stack) > 1 else stack[-1])
                sums += stack[-1]
        return sums
