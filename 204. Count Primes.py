Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
  
  class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n<=2:return 0
        
        cnt = 0
        arr = [True] * n
        sqrt = int(n**0.5)+1
        
        for i in range(2, sqrt):
            if arr[i] is True:
                cnt+=1
                for j in range(i+i, n, i):
                    arr[j]=False
                    
        for i in range(sqrt, n):
            if arr[i] is True:
                cnt+=1

        return cnt
