"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.
"""

class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        nums = {}
        for i in A:
            if i not in nums:
                nums[i]= 0
            else:
                return i
