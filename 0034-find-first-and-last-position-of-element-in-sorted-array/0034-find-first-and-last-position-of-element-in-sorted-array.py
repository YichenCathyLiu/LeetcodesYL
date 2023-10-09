class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        position = [-1,-1]
        result = [x == target for x in nums]

        print(result)

        if (True in result)==1:
            position = []
            for i in range(len(result)):
                if result[i] == True:
                    position.append(i)
        
        if len(position)<2:
            position = [position[0]]*2
        elif len(position)>2:
            position = [position[0],position[-1]]
        return position

        