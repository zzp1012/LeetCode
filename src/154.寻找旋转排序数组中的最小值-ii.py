#
# @lc app=leetcode.cn id=154 lang=python
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] < nums[-1]:
            return nums[0]

        if nums == []:
            return -1
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums[0], nums[1])

        mid = len(nums) // 2
        if nums[-1] < nums[mid]:
            return self.findMin(nums[mid+1:])
        elif nums[-1] == nums[mid]:
            return min(self.findMin(nums[mid+1:]), self.findMin(nums[:mid+1]))        
        else:
            return self.findMin(nums[:mid+1])
# @lc code=end

