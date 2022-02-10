An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

 

Example 1:


Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.



class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        summ = 0
        lst = []
        checking = []
        for i in range(1, n+1):
            summ += i
            lst.append(i)
        for x in range(n):
            if sorted(matrix[x]) != lst:
                return False
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                checking.append(matrix[j][i])
            checking = sorted(checking)
            print(checking)
            if checking != lst:
                return False
            checking = []
        return True
