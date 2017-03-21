class Solution(object):
    def singleNumber(self, nums):
        # Given an array of integers, every element appears twice except for one. Find that single one.
        # type nums: List[int]
        # rtype: int
        
        return sum(list(set(nums)))*2 - sum(nums)
