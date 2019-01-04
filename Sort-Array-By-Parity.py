"""
Given an array A of non-negative integers,
return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
"""



class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        start = 0
        end = len(A) - 1
        while start < end:
            if A[start] % 2 != 0:
                odd = A[start]
                A[start] = A[end]
                A[end] = odd
                end -= 1
            else:
                start += 1
        return A
        
 #Brute Force
 
 class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = []
        C = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                B.append(A[i])
            else:
                C.append(A[i])
        return B+C
