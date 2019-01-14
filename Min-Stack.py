"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack:

    def __init__(self):
        self.items = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.items.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.items.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[len(self.items)-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.items)
