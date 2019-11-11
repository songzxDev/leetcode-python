# -*- coding: utf-8 -*-
# @Time    : 2019-11-11 08:38
# @Author  : songzhenxi
# @Email   : songzx_2326@163.com
# @File    : solution.py
# @Software: PyCharm


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
    # 注意：答案中不可以包含重复的三元组。
    #
    # 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
    #
    # 满足要求的三元组集合为：
    # [
    #  [-1, 0, 1],
    #  [-1, -1, 2]
    # ]
    #
    # Related Topics 数组 双指针
    def threeSum(self, nums):
        """
        题目：15.三数之和
        标签：数组 双指针
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for k, num in enumerate(nums):
            if num > 0:
                break
            if (k == 0 or nums[k] != nums[k - 1]) and k < len(nums) - 2:
                left, right = k + 1, len(nums) - 1
                while left < right:
                    sumnum = num + nums[left] + nums[right]
                    if sumnum == 0:
                        res.append([num, nums[left], nums[right]])
                        leftnum, rightnum = nums[left], nums[right]
                        left += 1
                        while left < right and leftnum == nums[left]:
                            left += 1
                        right -= 1
                        while left < right and rightnum == nums[right]:
                            right -= 1
                    elif sumnum < 0:
                        leftnum = nums[left]
                        left += 1
                        while left < right and leftnum == nums[left]:
                            left += 1
                    else:
                        rightnum = nums[right]
                        right -= 1
                        while left < right and rightnum == nums[right]:
                            right -= 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
