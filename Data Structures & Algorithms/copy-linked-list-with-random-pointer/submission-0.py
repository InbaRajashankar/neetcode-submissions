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

        # create copies of each node without replicating random
        # store orig -> cpy mappings in dict
        m = {}
        new_head = Node(0)
        tmp = new_head

        cur = head
        while cur is not None:
            tmp.next = Node(cur.val, cur.next)
            tmp = tmp.next
            m[cur] = tmp
            cur = cur.next


        # populate random pointers using dict
        i = head
        j = new_head.next
        while i is not None:
            if i.random:
                j.random = m[i.random]
            i = i.next
            j = j.next
        
        return new_head.next

        