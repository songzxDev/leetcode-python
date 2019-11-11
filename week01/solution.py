# -*- coding: utf-8 -*-
# @Time    : 2019-11-11 08:38
# @Author  : songzhenxi
# @Email   : songzx_2326@163.com
# @File    : solution.py
# @Software: PyCharm


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    # 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
    #
    # 示例 1:
    #
    # 输入: s = "anagram", t = "nagaram"
    # 输出: true
    #
    #
    # 示例 2:
    #
    # 输入: s = "rat", t = "car"
    # 输出: false
    #
    # 说明:
    # 你可以假设字符串只包含小写字母。
    #
    # 进阶:
    # 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
    # Related Topics 排序 哈希表
    def isAnagram(self, s, t):
        """
        题目：242.有效的字母异位词
        标签：排序 哈希表
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

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

    # 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    #
    # 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
    #
    # 示例:
    #
    # 给定 nums = [2, 7, 11, 15], target = 9
    #
    # 因为 nums[0] + nums[1] = 2 + 7 = 9
    # 所以返回 [0, 1]
    #
    # Related Topics 数组 哈希表
    def twoSum(self, nums, target):
        """
        题目：1.两数之和
        标签：数组 哈希表
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = {}
        for i, n in enumerate(nums):
            sub = target - n
            if sub in tmp:
                return [tmp[sub], i]
            else:
                tmp[n] = i
        return []

    # 示例 2:
    #
    # 输入:pattern = "abba", str = "dog cat cat fish"
    # 输出: false
    #
    # 示例 3:
    #
    # 输入: pattern = "aaaa", str = "dog cat cat dog"
    # 输出: false
    #
    # 示例 4:
    #
    # 输入: pattern = "abba", str = "dog dog dog dog"
    # 输出: false
    #
    # 说明:
    # 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。
    # Related Topics 哈希表
    def wordPattern(self, pattern, ss):
        """
        题目：290.单词规律
        标签：哈希表
        :type pattern: str
        :type ss: str
        :rtype: bool
        """
        pndt, ssdt, sslst = {}, {}, ss.split(' ')
        if len(pattern) != len(sslst):
            return False
        for idx, ch in enumerate(pattern):
            if pndt.get(ch) != ssdt.get(sslst[idx]):
                return False
            pndt[ch], ssdt[sslst[idx]] = idx, idx
        return True

# leetcode submit region end(Prohibit modification and deletion)
