
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        max_len = 0
        nums = set(nums)
        
        for n in nums:
            if (n-1) not in nums:
                length = 1
                while (n+length) in nums:
                    length += 1
                max_len = max(length, max_len)
        return max_len
        