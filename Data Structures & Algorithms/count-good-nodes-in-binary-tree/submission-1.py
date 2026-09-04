# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = deque()
        stack.append((root.val, root)) # (path_max, vertex)

        good_nodes = 0

        encoded = deque()

        while stack:
            cur_max, cur = stack.pop()

            if cur.val >= cur_max or cur == root:
                good_nodes += 1

            new_max = max(cur.val, cur_max)
            if cur.left:
                stack.append((new_max, cur.left))
            if cur.right:
                stack.append((new_max, cur.right))

        return good_nodes



        