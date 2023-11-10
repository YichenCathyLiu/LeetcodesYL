class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = len(nums1)
        n = len(nums2)
        result = []

        if m<n :
            for i in nums1:
                if i in nums2:
                    result.append(i)
        else:
            for i in nums2:
                if i in nums1:
                    result.append(i)

        return list(set(result))
        