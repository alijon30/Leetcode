


he Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.

 

Example 1:



Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.
Example 2:



Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3
Example 3:

Input: logs = ["d1/","../","../","../"]
Output: 0




class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = Stack()
        
        for i in range(len(logs)):
            if logs[i] == "../":
                stack.pop()
            elif logs[i] == "./":
                continue
            elif logs[i] == "x/":
                stack.push("X")
            else:
                stack.push(logs[i])
        count = 0
        while not stack.isEmpty():
            count += 1
            stack.pop()
        
        return count
        
        
        
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
        
class Stack:
    def __init__(self):
        self.Linked = LinkedList()
    
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.Linked.head
        self.Linked.head = newNode
    
    def isEmpty(self):
        if self.Linked.head == None:
            return True
        else:
            return False
    
    def pop(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            node = self.Linked.head.value
            self.Linked.head = self.Linked.head.next
            return node
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            node = self.Linked.head.value
            return node
            
            
            
            
            
