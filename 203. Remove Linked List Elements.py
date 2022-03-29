Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []



Version 1
class Solution:

def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    while head != None and head.val == val:
        head= head.next
    print(head)
    current_node = head
    while current_node != None and current_node.next != None:
        if current_node.next.val == val:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
        
    return head
Version 2

new = ListNode(next = head)
prev, curr = new, head

    while curr:
        nxt =curr.next
        
        if curr.val == val:
            prev.next = nxt
        else:
            prev = curr
        curr = nxt
    
    return new.next
  
  
  
