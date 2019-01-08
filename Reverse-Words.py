"""
Given a string, you need to reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.

Example:

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

"""

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(x[::-1] for x in s.split())
