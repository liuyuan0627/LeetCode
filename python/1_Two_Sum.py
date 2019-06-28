class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Solution 1
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        """
        
        # Solution 2
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                j = nums[i+1:].index(target - nums[i])
                return [i, i+j+1]
