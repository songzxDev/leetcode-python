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

    # 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    # 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    # 注意：给定 n 是一个正整数。
    # 示例 1：
    # 输入： 2
    # 输出： 2
    # 解释： 有两种方法可以爬到楼顶。
    # 1.  1 阶 + 1 阶
    # 2.  2 阶
    # 示例 2：
    # 输入： 3
    # 输出： 3
    # 解释： 有三种方法可以爬到楼顶。
    # 1.  1 阶 + 1 阶 + 1 阶
    # 2.  1 阶 + 2 阶
    # 3.  2 阶 + 1 阶
    # Related Topics 动态规划
    def climbStairs(self, n):
        """
        题目：70.爬楼梯
        标签：数组 数学 动态规划
        :type n: int
        :rtype: int
        """
        i, tmp = 3, {1: 1, 2: 2}
        while i <= n:
            tmp[i], i = tmp[i - 1] + tmp[i - 2], i + 1
        return tmp[n]

    # 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
    # 示例：
    #
    # 输入: ["Hello", "Alaska", "Dad", "Peace"]
    # 输出: ["Alaska", "Dad"]
    # 注意：
    #
    # 你可以重复使用键盘上同一字符。
    # 你可以假设输入的字符串将只包含字母。
    # Related Topics 哈希表
    def findWords(self, words):
        """
        题号：500.键盘行
        标签：哈希表
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = {"Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
        set2 = {"A", "S", "D", "F", "G", "H", "J", "K", "L", "a", "s", "d", "f", "g", "h", "j", "k", "l"}
        set3 = {"Z", "X", "C", "V", "B", "N", "M", "z", "x", "c", "v", "b", "n", "m"}
        res = []
        for word in words:
            wdset = set(word)
            if wdset <= set1 or wdset <= set2 or wdset <= set3:
                res.append(word)
        return res

    # 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
    # 有效字符串需满足：
    # 左括号必须用相同类型的右括号闭合。
    # 左括号必须以正确的顺序闭合。
    # 注意空字符串可被认为是有效字符串。
    # 示例 1:
    # 输入: "()"
    # 输出: true
    # 示例 2:
    # 输入: "()[]{}"
    # 输出: true
    # 示例 3:
    # 输入: "(]"
    # 输出: false
    # 示例 4:
    # 输入: "([)]"
    # 输出: false
    # 示例 5:
    # 输入: "{[]}"
    # 输出: true
    # Related Topics 栈 字符串
    def isValid(self, ss):
        # 时间复杂度为：O(N^2)的写法，不停的替换成对的括号，直到不存在成对为止
        def replace_brackets(replstr):
            while '()' in replstr or '[]' in replstr or '{}' in replstr:
                replstr = replstr.replace('()', '').replace('[]', '').replace('{}', '')
            return replstr

        """
        题目：20.有效的括号
        标签：栈 字符串
        :type s: str
        :rtype: bool
        """
        stack = []
        for s in ss:
            if s == '(':
                stack.append(')')
            elif s == '{':
                stack.append('}')
            elif s == '[':
                stack.append(']')
            elif len(stack) == 0 or stack.pop() != s:
                return False
        return len(stack) == 0

    # 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
    # 案例:
    # s = "leetcode"
    # 返回 0.
    # s = "loveleetcode",
    # 返回 2.
    # 注意事项：您可以假定该字符串只包含小写字母。
    # Related Topics 哈希表 字符串
    def firstUniqCharSlow(self, s):
        """
        题目：387.字符串中的第一个唯一字符
        标签：哈希表 字符串
        :type s: str
        :rtype: int
        """
        counts = [0] * 26
        for c in s:
            counts[ord(c) - 97] += 1
        for i in xrange(len(s)):
            if counts[ord(s[i])-97] == 1:
                return i
        return -1

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # python 正好和js、java相反，哈希表比数组遍历快
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        for i in xrange(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1

    def firstuniqchar(self, s):
        """
        题目：387.字符串的第一个唯一字符
        标签：哈希表 字符串（风骚解法）
        :type s: str
        :rtype: int
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        idxs = [s.index(ltt) for ltt in letters if s.count(ltt) == 1]
        return min(idxs) if len(idxs) > 0 else -1

# leetcode submit region end(Prohibit modification and deletion)
