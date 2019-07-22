class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # solution 1
        if val in nums:
            nums.sort()
            h = nums.index(val)
            t = nums[::-1].index(val)
            del nums[h:len(nums)-t]
        return len(nums)
    
        # solution 2
        """
        i = 0
        while i != len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
        """
        
"""
list.sort()
list.index(x), return the smallest i such that i is the index of the first occurrence of x in the array
list.pop(i), removes the item with the index i from the array and returns it. The optional argument defaults to -1, so that by default the last item is removed and returned.
del list[index]
"""
