class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        currBinary, result = 0, []
        for bit in nums:
            currBinary = (currBinary * 2 + bit) % 5 
            result.append(currBinary == 0)
        return result