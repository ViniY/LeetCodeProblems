class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, a: ListNode, b:ListNode):
        # head = sort_list = ListNode(0)
        #
        # while(a and b):
        #     if ( a.val >= b.val):
        #         sort_list.next = b
        #         b = b.next
        #         sort_list = sort_list.next
        #     else:
        #         sort_list.next = a
        #         a = a.next
        #         sort_list = sort_list.next
        # sort_list.next = a or b
        # return head.next
        #
        if a and b: # both a and b not none
            if a.val > b.val:
                a,b = b,a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b


if __name__ == '__main__':
    sol = Solution()
    sol.mergeTwoLists([1, 2, 4], [1, 3, 4])