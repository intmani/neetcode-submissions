# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        if not list1:
            return list2
        
        if not list2:
            return list1
        
        l1 = list1
        l2 = list2
        dummy = ListNode()
        tail = dummy

        while (l1 != None) and (l2 != None):

            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
                tail = tail.next
            
            else:
                tail.next = l2
                l2 = l2.next
                tail = tail.next
        
        tail.next = l1 if l1 else l2
        return dummy.next
