# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque() # (node, min, max)
        q.append((root, None, None))

        while q:
            cur, cur_min, cur_max = q.popleft()

            if cur_min is not None and cur.val <= cur_min:
                return False
            if cur_max is not None and cur.val >= cur_max:
                return False

            if cur.left:
                q.append((cur.left, cur_min, cur.val))
            if cur.right:
                q.append((cur.right, cur.val, cur_max))
        
        return True

        