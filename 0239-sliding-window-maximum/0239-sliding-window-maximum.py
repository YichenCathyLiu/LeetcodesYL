class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mq = deque()
        maxes = []
        
        for i in range(len(nums)):            
            if mq and mq[0] <= i - k: mq.popleft()
            while mq and nums[mq[-1]] <= nums[i]: mq.pop()
            
            mq.append(i)
            if i >= k - 1: maxes.append(nums[mq[0]])
        
        return maxes