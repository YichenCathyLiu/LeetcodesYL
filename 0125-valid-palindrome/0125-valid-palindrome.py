class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # solution1
        # first step: get all the alphabets and numbers
        # second step: check if it is palindrome

        # solution2: only compare if the letters are the same when they are letters or numbers
        # the key is two pointers 

        p1, p2 = 0, len(s)-1 # two pointers
        while p1 < p2:
            if s[p1].isalnum() == False:
                p1 = p1+1
            elif s[p2].isalnum() == False:
                p2 = p2-1
            elif s[p1].lower() == s[p2].lower():
                p1 = p1+1
                p2 = p2-1
            else:
                return False        
        return True