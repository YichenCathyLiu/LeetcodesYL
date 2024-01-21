class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        one_before = 2
        two_before = 1
        total = 0
        
        for i in range(1,n-1):
            total = one_before+two_before
            two_before = one_before
            one_before = total

        return total