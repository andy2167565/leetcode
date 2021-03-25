class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
#======== <Solution 1> ========#
        result = [[1]]
        if numRows == 1:
            return result
        for row_num in range(1, numRows):
            # First number of each row is 1
            row = [1]
            for j in range(1, row_num):
                # row_num-1: Iterate numbers in previous row
                # Add sequential pair of numbers
                row.append(result[row_num-1][j-1] + result[row_num-1][j]) 
            # Last number of each row is also 1
            row.append(1)
            result.append(row)
        return result
        
#======== <Solution 2> ========#
        # Create a triangle of all ones
        result = [[1]*(row_num+1) for row_num in range(numRows)]
        for row_num in range(numRows):
            for j in range(1, row_num):
                # Replace elements in the middle with sum of elements
                # above-and-to-the-left and above-and-to-the-right
                result[row_num][j] = result[row_num-1][j-1] + result[row_num-1][j]
        return result
        
#======== <Solution 3: Combinations> ========#
        # Each entry can be calculated by combinations formula
        from math import factorial
        C = lambda n, r: factorial(n) // factorial(r) // factorial(n - r)
        return [[C(n, r) for r in range(n + 1)] for n in range(numRows)]
