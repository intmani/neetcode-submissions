# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        storage = set()
        p = head

        while p != None:
            if p in storage:
                return True
            else:
                storage.add(p)
                p = p.next
        else:
            return False