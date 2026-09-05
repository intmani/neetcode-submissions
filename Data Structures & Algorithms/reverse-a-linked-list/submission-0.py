# Definition for singly-linked list.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        p = head
        q = None
        r = None

        while p != None:
            r = q
            q = p   
            p = p.next
            q.next = r
        
        head = q

        return q
