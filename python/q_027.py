class Solution(object):
    def removeElement(self, nums, val):
        # Given an array and a value, remove all instances of that value in place and return the new length.
        # Do not allocate extra space for another array, you must do this in place with constant memory.
        # type nums: List[int]
        # type val: int
        # rtype: int
        
        while True:
            try:
                nums.remove(val)
            except:
                return len(nums)
            
