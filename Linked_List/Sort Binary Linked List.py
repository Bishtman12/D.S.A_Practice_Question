#Question State
'''Given a Linked List A consisting of N nodes.
The Linked List is binary i.e data values in the linked list nodes consist of only 0's and 1's.
You need to sort the linked list and return the new linked list.'''
# Input  1 -> 0 -> 0 -> 1
# Output 0 -> 0 -> 1 -> 1
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        #dummy node to store the head of the list
        dummy = ListNode(None)
        dummy.next = A #now dummy is pointing to the head of the node

        #My Approach-> Count the no. of 0s and 1s in the input then revalue them.
        c_zero = 0
        c_one = 0
        head = A
        while head:
            if head.val == 0:
                c_zero +=1
            if head.val == 1:
                c_one +=1
            head = head.next
        head = A

        while head:
            if c_zero >= 0 :
                head.val = 0
                c_zero -=1
            if c_zero<0 :
                head.val = 1
            head = head.next
        strp = ' '
        while A:
            strp = strp + str(A.val) + "->"
            A = A.next
        return (f"Linked list:{strp}None")
head = ListNode(1)
second = ListNode(0)
third = ListNode(0)
four = ListNode(1)
sol = Solution()
head.next = second
second.next = third
third.next = four
four.next = None

print(sol.solve(head))
# Input  1 -> 0 -> 0 -> 1