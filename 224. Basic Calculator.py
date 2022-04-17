
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23




class Solution:
    def calculate(self, s: str) -> int:
        
        value = 0
        sign = 1
        
        stack = Stack()
        i = 0
        
        while i < len(s):
            if s[i].isnumeric():
                
                num = 0
                while i < len(s) and s[i].isnumeric():
                    num = num * 10 + int(s[i])
                
                    i += 1
                value += num * sign
                i -= 1
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            elif s[i] == "(":
                stack.push(value)
                stack.push(sign)
                value = 0
                sign = 1
            elif s[i] == ")":
                value = stack.pop() * value
                value += stack.pop()
            i += 1
        return value
    
        
class Stack:
    def __init__(self):
        self.list = []
    
    def push(self, value):
        self.list.append(value)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    def pop(self):
        if self.isEmpty():
            return "NO"
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "No"
        else:
            return self.list[-1]
          
          
          
