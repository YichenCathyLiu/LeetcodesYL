class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        s_freq = {}
        t_freq = {}
        for char in s:
            if char in s_freq.keys():
                s_freq[char] = s_freq[char]+1
            else:
                s_freq[char] = 1
        for char in t:
            if char in t_freq.keys():
                t_freq[char] = t_freq[char]+1
            else:
                t_freq[char] = 1
        return s_freq == t_freq  