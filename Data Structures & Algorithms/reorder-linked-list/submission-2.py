# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = valnet
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle node
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # break the list into two
        second = slow.next
        slow.next = None

        # reverse the second list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge the two lists with condition
        second = prev 
        first = head
        while second:
            t1 = first.next
            t2 = second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2
        


        
        
        

