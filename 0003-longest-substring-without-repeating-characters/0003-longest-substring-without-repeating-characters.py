class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 1:
            return 1
        result = 0
        j = 0
        seen = []

        while j <len(s):
            if (s[j] in seen) == False:
                print(j)
                seen.extend(s[j])
                j = j+1
            else:
                print(seen,j)
                result = max(len(seen),result)
                previous = seen.index(s[j])
                seen = seen[previous+1:]
                
        print(seen)
        return max(len(seen),result)