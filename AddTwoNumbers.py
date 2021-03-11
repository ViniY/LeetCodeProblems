# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = 0
        temp = l1
        count = 0
        num1 = 0
        num2 = 0
        while temp != None:
            num1 += temp.val * 10 ** count
            count += 1
            temp = temp.next

        count = 0
        temp = l2
        while temp != None:
            num2 += temp.val * 10 ** count
            count += 1
            temp = temp.next
        num = num1 + num2
        res = [int(x) for x in str(num)]
        r = []
        ll = len(res)
        for i in range(ll):
            temp = ListNode(val=res[ll - i - 1])
            r.append(temp)
        result = r[0]
        for i in range(ll - 1):
            r[i].next = r[i + 1]

        return result


if __name__ == '__main__':
    l1_3 = ListNode(val=3)
    l1_2 = ListNode(val=4,next=l1_3)
    l1_1 = ListNode(val=2,next=l1_2)
    l2_3 = ListNode(val=4)
    l2_2 = ListNode(val=6,next=l2_3)
    l2_1 = ListNode(val=5,next=l2_2)
    s = Solution()
    r = s.addTwoNumbers(l1_1,l2_1)
