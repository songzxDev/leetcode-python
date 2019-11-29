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

    def findDuplicate(self, nums):
        """
        题目：287.寻找重复数
        标签：数组 双指针
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0], nums[0]
        slow, fast = nums[slow], nums[nums[fast]]
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow

    # 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
    # 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
    # 注意:
    # 不能使用代码库中的排序函数来解决这道题。
    # 示例:
    # 输入: [2,0,2,1,1,0]
    # 输出: [0,0,1,1,2,2]
    # 进阶：
    # 一个直观的解决方案是使用计数排序的两趟扫描算法。
    # 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
    # 你能想出一个仅使用常数空间的一趟扫描算法吗？
    # Related Topics 排序 数组 双指针
    def sortColors(self, nums):
        """
        题目：75.颜色分类
        标签：数组 双指针
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        one, two = 0, 0
        for i in xrange(len(nums)):
            if nums[i] == 2:
                two += 1
            elif two > 0:
                nums[i], nums[i - two] = nums[i - two], nums[i]
        for j in xrange(len(nums) - two):
            if nums[j] == 1:
                one += 1
            elif one > 0:
                nums[j], nums[j - one] = nums[j - one], nums[j]
