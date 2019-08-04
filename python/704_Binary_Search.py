class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # solution 1
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) / 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m + 1
        return -1
        """
        # solution 2
        if target in nums:
            return nums.index(target)
        return -1
        """
        
