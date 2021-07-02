'''
https://www.interviewbit.com/problems/sum-of-fibonacci-numbers/
'''

class Solution:
    # @param A : integer
    # @return an integer
    def recfib (self, n, count = 1):
        if n == 0: return 0
        if n == 1: return 1
        p = 0
        s = 1
        res = p
        while p <= n:
            res = p
            tmp = s
            s = p + s
            p = tmp
            
        sheerit = n - res
        count = count + 1
        self.recfib(sheerit, count)
        return count

    def fibsum(self, A):
        return self.recfib(A)
        
