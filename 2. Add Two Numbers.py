from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number_1 = ""
        number_2 = ""
        node_l1 = l1
        node_l2 = l2
        
        while node_l1.next != None:
            number_1 = str(node_l1.val) + number_1
            node_l1 = node_l1.next
        if node_l1.next == None:
            number_1 = str(node_l1.val) + number_1
        while node_l2.next != None:
            number_2 = str(node_l2.val) + number_2
            node_l2 = node_l2.next
        if node_l2.next == None:
            number_2 = str(node_l2.val) + number_2
        sum_of_two = str(int(number_1) + int(number_2))
        
        for indx, digit in enumerate(sum_of_two):
            if indx == 0:
                node = ListNode(int(digit),None)
            else:
                node = ListNode(int(digit),node)
        return node
    




