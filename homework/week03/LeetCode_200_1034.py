# -*- coding: utf-8 -*-
# @Time    : 2019/12/28 0028 18:48
# @Author  : songzhenxi
# @Email   : songzx_2326@163.com
# @File    : LeetCode_200_1034.py
# @Software: PyCharm

# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
#
# 输出: 1
#
#
# 示例 2:
#
# 输入:
# 11000
# 11000
# 00100
# 00011
#
# 输出: 3
#
# Related Topics 深度优先搜索 广度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numIslands(self, grid):
        """
        题目：200.岛屿数量（https://leetcode-cn.com/problems/number-of-islands/）
        学号：1034（五期一班三组）
        :type grid: List[List[str]]
        :rtype: int
        """
        lands = 0
        if grid:
            for i in xrange(len(grid)):
                for j in xrange(len(grid[i])):
                    if grid[i][j] == '1':
                        lands += self.sink(i, j, grid)
        return lands

    def sink(self, i, j, grid):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0':
            return 0
        grid[i][j] = '0'
        self.sink(i - 1, j, grid)
        self.sink(i + 1, j, grid)
        self.sink(i, j - 1, grid)
        self.sink(i, j + 1, grid)
        return 1
# leetcode submit region end(Prohibit modification and deletion)
