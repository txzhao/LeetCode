class Solution(object):
    def searchInsert(self, nums, target):
        # Given a sorted array and a target value, return the index if the target is found. 
        # If not, return the index where it would be if it were inserted in order.
        # type nums: List[int]
        # type target: int
        # rtype: int
        
        for idx, value in enumerate(nums):
            if target <= value:
                return idx
            else:
                # check if 
                if idx >= len(nums) - 1:
                    return idx + 1
