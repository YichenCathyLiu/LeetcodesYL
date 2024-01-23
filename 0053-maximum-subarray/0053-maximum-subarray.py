class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsub = nums[0] # default result
        cumsum = 0

        for n in nums:
            cumsum = max(cumsum,0) 
            cumsum += n
            maxsub = max(maxsub, cumsum)
        return maxsub


