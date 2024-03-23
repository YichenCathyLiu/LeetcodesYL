class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r = 0,len(nums)-1 # 双指针
        result = [float('inf')] * len(nums)
        i = len(nums)-1
        while l<=r:
            if nums[l]**2> nums[r]**2: # 左大
                result[i] = nums[l]**2
                l = l+1
            else:
                result[i] = nums[r]**2
                r = r-1
            i = i-1
        return result

        