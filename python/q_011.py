class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        width = len(height) - 1
        area = 0
        
        for w in range(width, 0, -1):
            if height[left] < height[right]:
                area = max(area, height[left]*w)
                left += 1
            else:
                area = max(area, height[right]*w)
                right -= 1
        return area
