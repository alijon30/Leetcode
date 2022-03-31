You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
"C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
Return the sum of all the scores on the record.

 

Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
Example 2:

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = Stack()
        total = 0
        for i in range(len(ops)):
            if ops[i] == "C":
                stack.pop()
            elif ops[i] == "D":
                a = int(stack.peek())
                stack.push(str(a * 2))
            elif ops[i] == "+":
                a = int(stack.peek())
                stack.pop()
                b = int(stack.peek())
                stack.pop()
                
                c = a + b
                
                stack.push(b)
                
                stack.push(a)
                
                stack.push(c)
                

            else:
                stack.push(ops[i])
        
        while not stack.isEmpty():
            
            total += int(stack.peek())
            stack.pop()
        return total

        
        
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
    
    def isEmpty(self):
        if self.Linked.head == None:
            return True
        else:
            return False
    
    def push(self, value):
        newNode= Node(value)
        newNode.next = self.Linked.head
        self.Linked.head = newNode
    
    def pop(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            self.Linked.head = self.Linked.head.next
    
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            temp = self.Linked.head.value
            return temp
    
   Solution2:
    
    class Solution:
    def calPoints(self, ops: List[str]) -> int:
        lst = []
        for i in range(len(ops)):
            if ops[i] == "D":
                lst.append(lst[-1]*2)
            elif ops[i] == "C":
                lst.pop()
            elif ops[i] == "+":
                lst.append(lst[-1] + lst[-2])
            else:
                lst.append(int(ops[i]))
        
        return sum(lst)
       
       
       
       
    
    
