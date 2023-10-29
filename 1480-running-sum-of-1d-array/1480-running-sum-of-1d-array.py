class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        runsum = [0]*len(nums)

        for i in range(len(nums)):
            runsum[i] = sum(nums[0:i+1])
        return runsum
        