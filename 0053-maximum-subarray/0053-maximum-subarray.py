class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsub = nums[0] # default result
        cumsum = 0

        for n in nums: 
            cumsum = max(cumsum,0) # 舍弃小于0的部分累积求和
            cumsum += n # update 新的sum subarray
            maxsub = max(maxsub, cumsum) # update latest result
        return maxsub


