
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3=ListNode()
        nextadd=False
        while(l1.next!=None and l2.next!=None):
            if nextadd:
                l3.val=(l1.val+l2.val)%10+1
            else:
                l3.val=(l1.val+l2.val)%10
            if ((l1.val+l2.val)//10)==1:
                nextadd=True
            l3.next=ListNode()
            l3=l3.next
            l1=l1.next
            l2=l2.next

        if(l1.next!=None):
            if nextadd:
                l3.val=l1.val+ 1
            else:
                l3.val=l1.val

            l3.next=ListNode()
            l3=l3.next
            l1=l1.next
            while(l1.next!=None):
                l3.val=l1.val
                l3.next=ListNode()
                l3=l3.next
                l1=l1.next

        if(l2.next!=None):
            if nextadd:
                l3.val=l2.val+ 1
            else:
                l3.val=l2.val

            l3.next=ListNode()
            l3=l3.next
            l2=l2.next
            while(l2.next!=None):
                l3.val=l2.val
                l3.next=ListNode()
                l3=l3.next
                l2=l2.next

        return l3

Solution().addTwoNumbers()