class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 1:
            low, up = 1, x
        elif x<1:
            low, up = 0, 1
        else:
            return 1

        while low<=up:
            mid = (low + up) // 2
            if mid * mid < x:
                low = mid + 1
            elif mid * mid > x:
                up = mid -1
            else:
                return mid

        return int((low+up)/2)