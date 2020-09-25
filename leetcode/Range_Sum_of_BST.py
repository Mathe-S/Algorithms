# XOR Operation in an Array

def xorOperation(n, start):
        ans = start
        for i in range(1, n):
            ans = (start + 2*i) ^ ans
            
        return ans



# Split a String in Balanced Strings

def balancedStringSplit(s):
        ans = 0
        count = 0
        for x in range(len(s)):
            count += 1  if s[x] == 'L' else -1
                
            if count == 0:
                ans +=1
            
        return ans



# Range Sum of BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)
        
        self.ans = 0
        dfs(root)
        
        return self.ans