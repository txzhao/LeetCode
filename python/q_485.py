class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        # Given a binary array, find the maximum number of consecutive 1s in this array.
        # type nums: List[int]
        # rtype: int
               
        maxlen, curlen = 0, 0
        
        for num in nums:
            if num == 1:
                curlen += 1
                maxlen = max(maxlen, curlen)
            else:
                curlen = 0
                
        return maxlen 
