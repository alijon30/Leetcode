

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        Dict = {}
        
        while head != None:
            if head.val not in Dict.keys():
                Dict[head.val] = 1
            else:
                Dict[head.val] += 1
            head = head.next
        for val1, val2 in Dict.items():
            if val2 == 1:
                curr.next = ListNode(val1)
                curr = curr.next
        return dummy.next
                
                
                
                
                
                
        
