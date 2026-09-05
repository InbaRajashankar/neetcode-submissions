# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        gain = {}

        stack = [(root, False)]
        result = float("-inf")

        while stack:
            node, visited = stack.pop()

            if node is None:
                continue
            
            if not visited: # process children first
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
            else:
                left_gain = max(gain.get(node.left, 0), 0)
                right_gain = max(gain.get(node.right, 0), 0)

                # Best path whose highest node is `node`.
                through_node = node.val + left_gain + right_gain
                result = max(result, through_node)

                # Gain that can be passed to the parent.
                gain[node] = node.val + max(left_gain, right_gain)
        
        return result



        