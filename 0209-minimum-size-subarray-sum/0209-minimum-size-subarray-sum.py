import sys

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # 滑动窗口sliding window法
        # 只用一层循环，循环体表示子列的最后一个元素，保持子列的和大于等于target
        result = sys.maxsize
        i = 0
        sum_value = 0
        
        for j in range(len(nums)):
            sum_value += nums[j]
            while sum_value >= target:  # 保持滑动窗口的sum一直大于等于target
                result = min(result, j - i + 1)
                sum_value -= nums[i]
                i += 1

        return result if result != sys.maxsize else 0