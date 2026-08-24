# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sln = ListNode()
        head = sln

        l1 = list1
        l2 = list2

        while l1 or l2:
            if not l1:
                sln.next = l2
                sln = sln.next
                break
            elif not l2:
                sln.next = l1
                sln = sln.next
                break
            elif l1.val < l2.val:
                sln.next = l1
                l1 = l1.next
            else: 
                sln.next = l2
                l2 = l2.next
            sln = sln.next
        
        return head.next
        