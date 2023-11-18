
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r

        return length

        '''
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
        '''