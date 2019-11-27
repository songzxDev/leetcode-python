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

    # 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
    # 示例 1：
    # 输入：[-4,-1,0,3,10]
    # 输出：[0,1,9,16,100]
    # 示例 2：
    # 输入：[-7,-3,2,3,11]
    # 输出：[4,9,9,49,121]
    # 提示：
    # 1 <= A.length <= 10000
    # -10000 <= A[i] <= 10000
    # A 已按非递减顺序排序。
    # Related Topics 数组 双指针
    def sortedSquares(self, A):
        """
        题目：977.有序数组的平方
        标签：数组 双指针
        :type A: List[int]
        :rtype: List[int]
        """
        if A is None or len(A) == 0:
            return []
        if A[0] >= 0:
            return map(lambda x: x * x, A)
        i, j, p, res = 0, len(A) - 1, len(A) - 1, [0] * len(A)
        while p >= 0:
            if abs(A[i]) > abs(A[j]):
                res[p], i = A[i] * A[i], i + 1
            else:
                res[p], j = A[j] * A[j], j - 1
            p -= 1
        return res
