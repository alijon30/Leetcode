The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
  
  
Class Solution:
  def fib(self, n, memo = {}):
    if n in memo.keys():
      return memo[n]
    if n == 0:
      return 0
    elif n in [1,2]:
      return n = 1
    else:
      memo[n] = self.fib(n-1) + self.fib(n-2)
      return memo[n]
     
     
     
