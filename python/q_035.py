class Solution(object):
    def searchInsert(self, nums, target):
        # Given a sorted array and a target value, return the index if the target is found. 
        # If not, return the index where it would be if it were inserted in order.
        # type nums: List[int]
        # type target: int
        # rtype: int
        
        # check if target is larger than the maximum in the sorted lise given
        if target > nums[-1]:
            return len(nums)
        
        for idx, value in enumerate(nums):
            if target <= value:
                return idx
            
