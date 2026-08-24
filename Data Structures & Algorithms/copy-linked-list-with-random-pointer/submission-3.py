"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head: 
            return None

        # create copies of each node without replicating random
        # store orig -> cpy mappings in dict
        m = {}

        cur = head
        while cur:
            tmp = Node(cur.val)
            m[cur] = tmp
            cur = cur.next

        # populate random pointers using dict
        cur = head
        while cur:
            if cur.next:
                m[cur].next = m[cur.next]
            if cur.random:
                m[cur].random = m[cur.random]
            cur = cur.next
        
        return m[head]

        