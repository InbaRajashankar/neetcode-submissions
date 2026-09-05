# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], left+root.val+right, root.val)

            gain = max(left, right, 0)
            # print(root.val, res[0], left, right)
            return root.val+gain
        
        res[0] = max(dfs(root), res[0])
        return res[0]

        