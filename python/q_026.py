class Solution(object):
    def removeDuplicates(self, nums):
        # Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
        # type nums: List[int]
        # rtype: int
        
        nums[:] = sorted(list(set(nums)))
        return len(nums)
