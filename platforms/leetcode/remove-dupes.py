from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        nextPtr = head.next
        currPtr = head
        while nextPtr is not None:
            if nextPtr.val != currPtr.val:
                currPtr.next = nextPtr
                currPtr = nextPtr
            nextPtr = nextPtr.next
        currPtr.next = None
        return head
