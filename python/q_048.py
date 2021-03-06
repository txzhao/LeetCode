class Solution(object):
    def rotate(self, matrix):
        # You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).
        # type matrix: List[List[int]]
        # rtype: void Do not return anything, modify matrix in-place instead.
        
        # rotate 90 degrees = first flip upside down, and then transpose
        matrix[:] = map(list, zip(*matrix[::-1]))
