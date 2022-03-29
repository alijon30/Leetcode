You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"




class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = Stack()
        for i in range(len(s)):
            if stack.peek() == s[i]:
                stack.pop()
                continue
            stack.push(s[i])
        print(stack)
        return str(stack)
            
    
class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(value) for value in self.list]
        return ''.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            return self.list[len(self.list)-1]

         
         
         
         
         
         ---------------------------------------
         
         
         class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = Stack()
        
        for i in range(len(s)):
            if stack.peek() == s[i]:
                stack.pop()
                continue
            stack.push(s[i])
        
        return str(stack)[::-1]
        
        
class Node:
    def __init__(self, value):
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
    
    def __str__(self):
        values = [str(val.value) for val in self.Linked]
        return ''.join(values)

        
    def isEmpty(self):
        if self.Linked.head == None:
            return True
        else:
            return False
    
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.Linked.head
        self.Linked.head = newNode
    
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            temp = self.Linked.head
            self.Linked.head = self.Linked.head.next
            return temp
    def peek(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            node = self.Linked.head.value
            return node
        
        

          
          
          
          
