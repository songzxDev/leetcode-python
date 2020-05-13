# -*- coding: utf-8 -*-
# @Time    : 2020-05-13 15:54
# @Author  : songzhenxi
# @Email   : songzx_2326@163.com
# @File    : leetcode912.py
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
        if nums and len(nums) > 1:
            self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def partition(self, nums, begin, end):
        pivot, counter = end, begin
        for i in range(begin, end):
            if nums[i] < nums[pivot]:
                nums[counter], nums[i] = nums[i], nums[counter]
                counter += 1
        nums[counter], nums[pivot] = nums[pivot], nums[counter]
        return counter

    def quicksort(self, nums, begin, end):
        if begin < end:
            pivot = self.partition(nums, begin, end)
            self.quicksort(nums, begin, pivot - 1)
            self.quicksort(nums, pivot + 1, end)
# leetcode submit region end(Prohibit modification and deletion)
