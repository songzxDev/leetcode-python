# 浅解题目：[189.旋转数组](https://leetcode-cn.com/problems/rotate-array/)
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。  
输入: [1,2,3,4,5,6,7] 和 k = 3  
输出: [5,6,7,1,2,3,4]   
向右旋转 1 步: [7,1,2,3,4,5,6]   
向右旋转 2 步: [6,7,1,2,3,4,5]   
向右旋转 3 步: [5,6,7,1,2,3,4] 
### 直观理解
根据 k 的值将 后面的 k 个元素按照顺序依次放置于数组前面，非移动元素依次后移，直觉可以用暴力法解决，时间复杂度:O(n ^ 2)。  
执行用时：296ms，在javascript中击败了8.39%的用户，显然效率不是最优的。      
```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const rotate = function(nums, k) {
    k %= nums.length;
    for (let i = 0; i < k; i++) {
        let p = nums.length - 1, currLast = nums[p];
        while (p > 0) {
            nums[p] = nums[--p];
        }
        nums[0] = currLast;
    }
};
```  
### 尝试寻找最近重复相关性
k = 1, [7, 1, 2, 3, 4, 5, 6]   
k = 2, [6, 7, 1, 2, 3, 4, 5]   
k = 3, [5, 6, 7, 1, 2, 3, 4]   
k = 4, [4, 5, 6, 7, 1, 2, 3]   
k = 5, [3, 4, 5, 6, 7, 1, 2]   
k = 6, [2, 3, 4, 5, 6, 7, 1]   
k = 7, [1, 2, 3, 4, 5, 6, 7]   
k = 8, [7, 1, 2, 3, 4, 5, 6]  
k = ?, .......   
#### Subtle 的解法
 1. 首先如果 k %= nums.length > 0，则将原数组整体反转一次，以 [1, 2, 3, 4, 5, 6, 7] 为例，反转后可得到 [7, 6, 5, 4, 3, 2, 1]   
 2. 尝试寻找依据 k 值反转后的结果和整体反转后 [7, 6, 5, 4, 3, 2, 1] 之间的关系
    * k = 1, [7, 1, 2, 3, 4, 5, 6]&nbsp;&nbsp;&nbsp;&nbsp;[7, 6, 5, 4, 3, 2, 1]，k = 1，可以将索引[0, 0]和[1, 6]两个范围内的元素整体反转
    * k = 2, [6, 7, 1, 2, 3, 4, 5]&nbsp;&nbsp;&nbsp;&nbsp;[7, 6, 5, 4, 3, 2, 1]，k = 2，可以将索引[0, 1]和[2, 6]两个范围内的元素整体反转
    * k = 3, [5, 6, 7, 1, 2, 3, 4]&nbsp;&nbsp;&nbsp;&nbsp;[7, 6, 5, 4, 3, 2, 1]，k = 3，可以将索引[0, 2]和[3, 6]两个范围内的元素整体反转
    * k = 4, [4, 5, 6, 7, 1, 2, 3]&nbsp;&nbsp;&nbsp;&nbsp;[7, 6, 5, 4, 3, 2, 1]，k = 4，可以将索引[0, 3]和[4, 6]两个范围内的元素整体反转
    * k = 5, [3, 4, 5, 6, 7, 1, 2]&nbsp;&nbsp;&nbsp;&nbsp;[7, 6, 5, 4, 3, 2, 1]，k = 5，可以将索引[0, 4]和[5, 6]两个范围内的元素整体反转
    * k = 6, [2, 3, 4, 5, 6, 7, 1]&nbsp;&nbsp;&nbsp;&nbsp;[7, 6, 5, 4, 3, 2, 1]，k = 6，可以将索引[0, 5]和[6, 6]两个范围内的元素整体反转
    * k = 7, [1, 2, 3, 4, 5, 6, 7]&nbsp;&nbsp;&nbsp;&nbsp;[7, 6, 5, 4, 3, 2, 1]，k = 7，因为 k % nums.length 的值为0，故无需反转数组
    * k = 8, [7, 1, 2, 3, 4, 5, 6]&nbsp;&nbsp;&nbsp;&nbsp;[7, 6, 5, 4, 3, 2, 1]，k = 8，可以将索引[0, 0]和[1, 6]两个范围内的元素整体反转
    * k = ?, ......   
 3. 通过观察汇总最近重复相关性，可以将题目转化为：   
    * 先计算 k 的值， k = k % nums.length   
    * 如果 k > 0， 则数组整体反转
    * 对索引范围：[0, k - 1] 之间的元素整体反转
    * 对索引范围：[k, nums.length - 1] 之间的元素整体反转
    * 反转后得到的结果既是所求的最终结果 
      
执行用时：76ms，击败javascript用户86.29%，可以看出将问题转换后，时间复杂度为：O(n)
```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const rotate = function(nums, k) {
    k %= nums.length;
    if (k === 0 || nums.length < 2) {
        return;
    }
    const reverse = (array, begin, end) => {
        while (begin < end) {
            array[begin] ^= array[end];
            array[end] ^= array[begin];
            array[begin++] ^= array[end--];
        }
    };
    reverse(nums, 0, nums.length - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, nums.length - 1);
};
```

### 个人领悟
通过这道题学到了一种解题思路，就是将问题换一个思路去解决，将这个问题转换为若干子问题，并缩小取样数据，来观察和归纳数据的重复相关性，进而得到最终解决方案。
> 覃超：算法题目最终都会回归到：寻找最近重复子问题，以空间换时间等方式。