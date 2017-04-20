class Solution(object):
    def maxArea(self, height):
        # Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
        # n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
        # Find two lines, which together with x-axis forms a container, such that the container contains the most water.
        # type height: List[int]
        # rtype: int
        
        left, right, width, area = 0, len(height) - 1, len(height) - 1, 0
        
        for w in range(width, 0, -1):
            # if left height is smaller than right, then right height is fixed
            # e.g.height[0] < height[5], don't need to check area (0,1),(0,2),(0,3),(0,4) (S01,S02,S03,S04 < S05)
            if height[left] <= height[right]:
                area = max(area, height[left]*w)
                left += 1
            else:
                area = max(area, height[right]*w)
                right -= 1
        
        return area
