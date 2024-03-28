class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split()
        # print(lst)
        lst = lst[::-1]
        return ' '.join(lst)