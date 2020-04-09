# -*- coding: utf-8 -*-
# @Time    : 2020-04-09 08:25
# @Author  : songzhenxi
# @Email   : songzx_2326@163.com
# @File    : LeetCode_912_1034.py
# @Software: PyCharm

# 给你一个整数数组 nums，请你将该数组升序排列。
#
#
#
#
#
#
#  示例 1：
#
#  输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#
#
#  示例 2：
#
#  输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 50000
#  -50000 <= nums[i] <= 50000
#
#


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) < 2:
            return nums
        small, big = min(nums), max(nums)
        size = big - small + 1
        countlst = [0] * size
        for num in nums:
            countlst[num - small] += 1
        for i in range(1, size):
            countlst[i] += countlst[i - 1]
        tmp, f = list(nums), len(nums) - 1
        while f >= 0:
            k = countlst[tmp[f] - small] - 1
            nums[k] = tmp[f]
            countlst[tmp[f] - small], f = k, f - 1
        return nums
# leetcode submit region end(Prohibit modification and deletion)
