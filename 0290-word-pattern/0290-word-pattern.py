class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern = [i for i in pattern]
        s = s.split()
        mapping = set(zip(pattern,s))
        print(len(pattern)/2)

        if len(set(pattern))==len(set(s))==len(mapping) and len((pattern))==len((s)):
            return True
        else:
            return False