class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0 # default
        s_counter = Counter(s)
        #print(s_counter)
        N = len(s)
        flag = 0
        max_odd = 0
        for value in s_counter.values():
            if value%2 == 0:
                res += value
            else:
                flag = 1
                res += (value-1)

        return res+flag
