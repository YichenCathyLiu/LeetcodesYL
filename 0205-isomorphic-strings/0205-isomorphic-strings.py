class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p = zip(s,t)

        if len(set(p)) == len(set(s)) == len(set(t)):
            return True
        else:
            return False


        