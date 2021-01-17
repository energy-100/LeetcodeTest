# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        firstpoint=head
        secondpoint=head
        for i in range(n):
            if (firstpoint.next):
                firstpoint=firstpoint.next
            else:
                return head.next

        while(firstpoint.next):
            firstpoint=firstpoint.next
            secondpoint=secondpoint.next

        secondpoint.next=secondpoint.next.next
        return head