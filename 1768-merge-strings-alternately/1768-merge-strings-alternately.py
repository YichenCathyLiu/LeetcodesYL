class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ''
        i=0
        j=0
        while i < len(word1) or j <len(word2):
            if i < len(word1):
                result = result+word1[i]
                i = i+1
            if j < len(word2):
                result = result+word2[j]
                j = j+1
        return result