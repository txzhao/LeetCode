class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        xstart = 0
        xend = x
        
        while xstart <= xend:
            interval = xend - xstart + 1
            xmid = xstart + (interval - 1)/2
            if xmid*xmid <= x < (xmid + 1)*(xmid + 1):
                return xmid
            elif x < xmid*xmid:
                xend = xmid
            else:
                xstart = xmid + 1
        return xmid
