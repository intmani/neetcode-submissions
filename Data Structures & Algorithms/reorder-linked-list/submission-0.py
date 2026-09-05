# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        sec = slow.next
        slow.next = None

        p1 = head
        prev = None
        curr = sec

        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
        
        p1 = head
        p2 = prev
        
        while p2 != None:
            temp1 = p1.next
            temp2 = p2.next

            p1.next = p2
            p2.next = temp1

            p1 = temp1
            p2 = temp2