# PROBLEM 21 - MERGE TWO SORTED LISTS 
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Check if either of the lists is empty
        if not list1:
            return list2
        if not list2:
            return list1

        # Create a dummy node as the head of the merged list
        dummy = ListNode(0)
        curr = dummy

        # Pointers to traverse the lists
        ptr1 = list1
        ptr2 = list2

        # Merge the lists by comparing the values
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                curr.next = ptr1
                ptr1 = ptr1.next
            else:
                curr.next = ptr2
                ptr2 = ptr2.next
            curr = curr.next

        # Append the remaining nodes of the non-empty list
        curr.next = ptr1 if ptr1 else ptr2

        # Return the head of the merged list
        return dummy.next