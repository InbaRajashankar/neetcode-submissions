# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast is not None:
            fast = fast.next.next if fast.next else None
            slow = slow.next
            if fast == slow and fast is not None:
                return True
        
        return False
        