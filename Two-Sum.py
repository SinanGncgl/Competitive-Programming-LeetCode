"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

# O(n) 

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = dict()
        for i in range(len(nums)):
        	second_addend = target - nums[i]
        	if second_addend in res:
        		return [res[second_addend], i]
        	else:
        		res[nums[i]] = i
