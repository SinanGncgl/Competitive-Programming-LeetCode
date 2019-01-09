"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.

"""

def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        f0,f1 = 0,1
        
        if N == 0:
            return 0
        for i in range(2,N):
            fn = f0 + f1
            f0 = f1
            f1 = fn
        fn = f0 + f1
        return fn
        
