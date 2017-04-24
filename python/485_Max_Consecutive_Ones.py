class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = 0
        for num in nums:
            if num == 1:
                count = count + 1
            else:
                count = 0
            result = max(count, result)
        return result