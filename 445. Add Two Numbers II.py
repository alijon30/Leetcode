
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = ''
        nums2 = ''
        
        while l1 != None:
            nums1 += str(l1.val)
            l1 = l1.next
        while l2 != None:
            nums2 += str(l2.val)
            l2 = l2.next
            
        res = str(int(nums1) + int(nums2))
        
        dummy = curr = ListNode(res[0])
        
        for e in res:
            curr.next = ListNode(e)
            curr = curr.next
        
        return dummy.next
        
        
        
        
