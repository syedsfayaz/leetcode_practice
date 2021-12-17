class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Recursively print linked list
def linked_list_str(l):
    if l is None:
        return ''
    return str(l.val) + '->' + linked_list_str(l.next)

# Make first linked list.
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
print(linked_list_str(l1))

# Make second linked list.
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(linked_list_str(l2))
#
class Solution(object):
    def addTwoNumbers(l1, l2):
        carry = 0

        l3 = cur = ListNode(0)
        while l1 or l2 or carry:
            result = 0
            if carry:
                result += carry
                carry = 0
            if l1:
                result += l1.val
                l1 = l1.next
            if l2:
               result += l2.val
               l2 = l2.next
            if result > 9:
                carry = result // 10
                result = result % 10

            cur.next = ListNode(result)
            cur = cur.next
        return l3.next


r = Solution.addTwoNumbers(l1, l2)
print(linked_list_str(r))


# def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#     self.l1 = l1
#     self.l2 = l2
#     self.l3 = head = ListNode(0)
#     # self.l3.val = None
#     carry = 0
#     while self.l1 or self.l2 or carry:
#         result = 0
#         if carry:
#             result += carry
#             carry = 0
#         if self.l1:
#             result += self.l1.val
#             self.l1 = self.l1.next
#
#         if self.l2:
#             result += self.l2.val
#             self.l2 = self.l2.next
#
#         if result > 9:
#             carry = result // 10
#             result = result % 10
#         head.next = ListNode(result)
#         head = head.next
#     return self.l3.next


nums = [1, 2, 3, 4, 5]
#nums = ['abc', 'def', 'ghi', 'klm', 'nop']
#nums = 'stri.ng'
n = 123456

# def reversing(n):
#     rev = 0
#     while 0 < n:
#         d = n % 10
#         n = n // 10
#         rev = rev * 10 + d
#     return(rev)
#
# print(reversing(n))

# names = ['Corey', 'Fayaz', 'Dave']
#
# # for index, name in enumerate(names, start=0):
# #     print(index, name)
# for index in range(0,len(names),3):
#     print(names[index])






