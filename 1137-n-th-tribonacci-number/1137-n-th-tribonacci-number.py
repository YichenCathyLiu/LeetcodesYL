class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        zero = 0
        first = 1
        second = 1
        # 三次斐波那契
        note = [0,1,1]

        if n == 0:
            return 0
        elif n ==1:
            return 1
        elif n == 2:
            return 1

        for i in range(3,n+1):
            new = zero+first+second
            if i == n:
                return new
            note.append(new)
            zero = first
            first = second
            second = new