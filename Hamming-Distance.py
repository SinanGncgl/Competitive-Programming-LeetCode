"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
"""

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return sum( ((x ^ y) >> n) & 1 != 0 for n in range(32))
        
        
#2

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = x ^ y
        y = 0
        while x:
            y += 1
            x = x & (x - 1)
        return y

#3

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ham = 0
        while x or y:
            ham += (x % 2) ^ (y % 2)
            x //= 2
            y //= 2
        return ham
