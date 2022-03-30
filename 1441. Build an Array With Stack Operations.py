You are given an array target and an integer n.

In each iteration, you will read a number from list = [1, 2, 3, ..., n].

Build the target array using the following operations:

"Push": Reads a new element from the beginning list, and pushes it in the array.
"Pop": Deletes the last element of the array.
If the target array is already built, stop reading more elements.
Return a list of the operations needed to build target. The test cases are generated so that the answer is unique.

 

Example 1:

Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: 
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]
Example 2:

Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]
Example 3:

Input: target = [1,2], n = 4
Output: ["Push","Push"]
Explanation: You only need to read the first 2 numbers and stop.




class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = Stack()
        final = []
        for i in range(1, target[-1]+1):
            if i in target:
                stack.push(i)
                final.append("Push")
            else:
                stack.push(i)
                stack.pop()
                final.append("Push")
                final.append("Pop")
                
        return final
    
class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = [str(value) for value in self.list]
        return ''.join(values)
    
    def push(self, value):
        self.list.append(value)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list.pop()
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[-1]
            
            
            
