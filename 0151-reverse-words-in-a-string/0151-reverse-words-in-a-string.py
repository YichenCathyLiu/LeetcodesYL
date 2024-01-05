class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # split words
        words = s.split()
        #print(words)
        # reverse the order of words
        return ' '.join(words[::-1])
