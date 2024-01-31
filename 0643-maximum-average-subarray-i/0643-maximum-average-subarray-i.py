class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        result = float(-1000000.00000)
        # Calculate the sum of the first k elements
        curr_sum = sum(nums[:k])
        result = float(curr_sum)
        
        # Iterate through the remaining subarrays
        # 不要写太多[i for i in nums]这个会拉高时间复杂度，相当于又在遍历，在现有array的基础上加减
        for i in range(k, n):
            curr_sum += nums[i] - nums[i - k]  # Update the sum by adding the new element and subtracting the old one
            result = float(max(result, curr_sum))
        
        return result / k