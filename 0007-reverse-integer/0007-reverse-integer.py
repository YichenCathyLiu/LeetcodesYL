class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if abs(x)>(2**31)-1: # 2147483648
            return 0
        
        res = 0
        if x == 0:
            return 0
        elif x<0:
            signal = -1
            x = x*-1
        else:
            signal = 1

        while x>0:
            div = x%10
            x = x/10
            res = res*10+div
        return res*signal if abs(res*signal)<=(2**31)-1 else 0