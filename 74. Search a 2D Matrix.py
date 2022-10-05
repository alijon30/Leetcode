Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        def binary_search(array, target):
            start, end = 0, len(array)-1
            
            while start <= end:
                
                middle = start + (end-start)//2
                
                if array[middle] == target:
                    return True
                
                elif array[middle] > target:
                    end = middle - 1
                    
                elif array[middle] < target:
                    start = middle + 1
                    
            return False
        
        for row in range(len(matrix)):
            if binary_search(matrix[row], target):
                return True
            
        return False
        
        
        
