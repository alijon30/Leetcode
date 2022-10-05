Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false



class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        start, end = 0, num/2
        
        while start <= end:
            
            middle = (start + end)//2
            
            if middle * middle == num:
                return True
            elif middle * middle > num:
                end = middle -1
            
            elif middle * middle < num:
                start = middle + 1
                
        return False
        
        
        
