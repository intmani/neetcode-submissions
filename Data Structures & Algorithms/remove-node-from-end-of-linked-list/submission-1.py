# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        m = 0
        p = head
    
        while p != None :
            p = p.next
            k += 1
        
        m = k - n
        t = 0
        p = head
        q = None

        if k == 1 and n == 1:
            head = None
            return head
        
        elif m == 0:
            return head.next
    
        else:
            p = head
            q = None

            while m != t:
                q = p
                p = p.next
                t += 1
            
            q.next = p.next
            p.next = None

            return head
        