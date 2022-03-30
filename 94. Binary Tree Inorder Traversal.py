
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []




class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(rootNode, lst):
            if not rootNode:
                return
            helper(rootNode.left, lst)
            lst.append(rootNode.val)
            helper(rootNode.right, lst)
        
        lst = []
        helper(root, lst)
        return lst



