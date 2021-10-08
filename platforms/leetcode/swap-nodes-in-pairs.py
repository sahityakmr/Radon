# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        newTail = None
        newHead = None

        while head is not None and head.next is not None:
            tempTail = head
            head = head.next
            tempHead = head
            head = head.next
            tempHead.next = tempTail

            if newHead is None:
                newHead = tempHead
            else:
                newTail.next = tempHead
            newTail = tempTail

        if newHead is None:
            return head
        newTail.next = head
        return newHead
