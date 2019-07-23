class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution 1
        """
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)
        """
    
        # solution 2
        nums[:] = sorted(set(nums))
        return len(nums)
        
