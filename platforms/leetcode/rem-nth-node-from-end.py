from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slowPtr = head
        fastPtr = head
        count = 1

        while count < n:
            fastPtr = fastPtr.next
            count += 1

        if fastPtr.next is None:
            head = head.next
            return head

        slowPtr = head
        fastPtr = fastPtr.next

        while fastPtr.next is not None:
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next

        slowPtr.next = slowPtr.next.next
        return head
