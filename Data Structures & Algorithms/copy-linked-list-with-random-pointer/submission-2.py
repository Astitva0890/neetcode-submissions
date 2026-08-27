"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        old_to_new = {}
        curr = head
        while curr:
            new = Node(curr.val)
            old_to_new[curr] = new
            curr = curr.next

        curr = head
        while curr:
            new = old_to_new[curr]
            new.next = old_to_new.get(curr.next)
            new.random = old_to_new.get(curr.random)
            curr = curr.next
        return old_to_new[head]
        
