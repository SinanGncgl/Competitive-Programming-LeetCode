/*
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A". */

from collections import Counter

#O(n) Solution

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count_stone = Counter(S)
        count = 0
        for jewel in J:
            count += count_stone[jewel]
        return count
        
# Brute-force O(n^2) Solution

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for i in range(len(J)):
            for j in range(len(S)):
                if(J[i] == S[j] ):
                    count += 1
        return count
