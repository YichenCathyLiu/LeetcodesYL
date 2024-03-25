class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # use a double pointer: swap each char corresponding to each set of pointers
        left, right = 0, len(s)-1
        while left<right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left+=1
            right-=1
        return s