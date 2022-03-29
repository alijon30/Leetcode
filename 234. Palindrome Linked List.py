Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reversed_list(head):
            prev = None
            curr = head
            
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        
        fast = head
        slow = reversed_list(slow)
        
        while slow!= None:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
