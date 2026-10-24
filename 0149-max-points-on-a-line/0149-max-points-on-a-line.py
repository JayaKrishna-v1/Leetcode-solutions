from math import gcd
from collections import defaultdict

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:                     
            return n

        best = 2
        for i in range(n):                  
            x1, y1 = points[i]
            slopes = defaultdict(int)       

            for j in range(i + 1, n):       
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                g = gcd(dx, dy)             
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):   
                    dx, dy = -dx, -dy
                slopes[(dx, dy)] += 1

            if slopes:
                best = max(best, max(slopes.values()) + 1)   
        return best