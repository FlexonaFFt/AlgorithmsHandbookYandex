class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional
class Solution:
    def midevall(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.head:
            slow = slow.next
            fast = fast.next.next
        return slow