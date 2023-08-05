class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
#======== <Solution 1> ========#
        d1, d2 = abs(xCenter - (x2 + x1) / 2), abs(yCenter - (y2 + y1) / 2)  # Distances between centers of circle and rectangle in x, y direction
        h1, h2 = (x2 - x1) / 2, (y2 - y1) / 2  # Half of width and height of rectangle
        l1, l2 = max(0, d1 - h1), max(0, d2 - h2)  # It can be negative if circle is completely in rectangle
        return l1 * l1 + l2 * l2 <= radius * radius  # Pythagorean Theorem

#======== <Solution 2> ========#
        return (xCenter - min(max(x1, xCenter), x2))**2 + (yCenter - min(max(y1, yCenter), y2))**2 <= radius**2
