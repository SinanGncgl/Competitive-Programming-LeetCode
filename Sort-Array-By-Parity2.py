"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.
"""

#Brute Force

class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = [0]*len(A)
        left,right = 0,1
        for num in A:
            if num % 2 == 0:
                res[left] = num
                left += 2
            else:
                res[right] = num
                right += 2
                
        return res
