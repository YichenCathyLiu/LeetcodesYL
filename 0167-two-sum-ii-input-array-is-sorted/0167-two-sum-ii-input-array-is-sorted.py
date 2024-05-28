class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # solution 1: use the diary as normal two-sum
        # diary = {}

        # for i in range(len(numbers)):
        #     diff = target - numbers[i]
        #     if diff in diary.keys():
        #         return [diary[diff],i+1]
        #     else:
        #         diary[numbers[i]] = i+1

        # solution 2 : two pointers
        l, r = 0,len(numbers)-1
        while l < r:
            two_sum = numbers[l]+numbers[r]

            if two_sum > target:
                r -= 1
            elif two_sum < target:
                l += 1
            else:
                return [l+1,r+1]
        