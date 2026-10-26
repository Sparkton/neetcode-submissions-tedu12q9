# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        value = []
        curr = head
        while curr:
            value.append(curr)
            curr = curr.next

        curr = head
        n = (len(value) - 1) // 2
        for _ in range((len(value) - 1) // 2):
            nxt = curr.next
            last = value.pop()
            curr.next = last
            last.next = nxt
            curr = nxt

        value[-1].next = None