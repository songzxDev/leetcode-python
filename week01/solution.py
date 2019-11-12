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

    # 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
    #
    # 说明:
    #
    #
    # 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
    # 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
    #
    #
    # 示例:
    #
    # 输入:
    # nums1 = [1,2,3,0,0,0], m = 3
    # nums2 = [2,5,6],       n = 3
    #
    # 输出: [1,2,2,3,5,6]
    # Related Topics 数组 双指针
    def merge(self, nums1, m, nums2, n):
        """
        题号：88.合并两个有序数组
        标签：数组 双指针
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[0:n] = nums2[0:n]

    # 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    #
    # 示例:
    #
    # 输入: [0,1,0,3,12]
    # 输出: [1,3,12,0,0]
    #
    # 说明:
    #
    #
    # 必须在原数组上操作，不能拷贝额外的数组。
    # 尽量减少操作次数。
    #
    # Related Topics 数组 双指针
    def moveZeroes(self, nums):
        """
        题号：283.移动零
        标签：数组双指针
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

    # 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，
    # 垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
    # 说明：你不能倾斜容器，且 n 的值至少为 2。
    # 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

    # 示例:
    # 输入: [1,8,6,2,5,4,8,3,7]
    # 输出: 49
    # Related Topics 数组 双指针
    def maxArea(self, height):
        """
        题目：11.盛最多水的容器
        标签：数组 双指针
        :type height: List[int]
        :rtype: int
        """
        ans, i, j = 0, 0, len(height) - 1
        while i < j:
            if height[i] < height[j]:
                minhgt = height[i]
                i += 1
            else:
                minhgt = height[j]
                j -= 1
            ans = max(ans, (j - i + 1) * minhgt)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
