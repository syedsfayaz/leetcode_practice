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
        l3 = ListNode(None)
        cur = l3
        result = 0
        while l1 or l2 or carry:
            if l1 or l2:
                v1 = l1.val if l1 else 0
                v2 = l2.val if l2 else 0
                result = v1 + v2 + carry
                cur.next = ListNode(result % 10)
                carry = result // 10
                cur = cur.next
                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None
        return l3.next

        # carry = 0
        #
        # l3 = cur = ListNode(0)
        # while l1 or l2 or carry:
        #     result = carry
        #     ## This code is for optimizing solution
        #     if (not l1 or not l2) and not carry:
        #         cur.next = l1 or l2
        #         break
        #     if l1:
        #         result += l1.val
        #         l1 = l1.next
        #     if l2:
        #        result += l2.val
        #        l2 = l2.next
        #     carry = result // 10
        #     cur.next = ListNode(result % 10)
        #     cur = cur.next
        # return l3.next


r = Solution.addTwoNumbers(l1, l2)
print(linked_list_str(r))