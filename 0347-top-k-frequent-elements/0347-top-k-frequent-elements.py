import heapq
from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Build the frequency dictionary
        freq = defaultdict(int)
        for item in nums:
            freq[item] += 1
        
        # Step 2: Use a heap to find the top k elements
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Step 3: Extract elements from the heap
        result = [heapq.heappop(heap)[1] for _ in range(len(heap))]
        result.reverse()  # To return the result in descending order of frequency
        
        return result
