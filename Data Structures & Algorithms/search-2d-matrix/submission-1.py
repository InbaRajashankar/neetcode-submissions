class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        t = 0
        b = len(matrix)
        m = (t+b)//2

        while b-t > 1:
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] < target:
                t = m
            else:
                b = m
            m = (t+b)//2
        
        # t is the right i

        l = 0
        r = len(matrix[0])
        m = (l+r)//2

        while l < r:
            if matrix[t][m] == target:
                return True
            elif matrix[t][m] < target:
                l = m+1
            else:
                r = m
            m = (l+r)//2
        
        return False
        