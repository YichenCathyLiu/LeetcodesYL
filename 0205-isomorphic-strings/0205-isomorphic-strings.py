class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # dic = zip(s,t)
        # print(dic)
        # if len(set(dic)) == len(set(s)) == len(set(t)):
        #     return True
        # else:
        #     return False
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))


        