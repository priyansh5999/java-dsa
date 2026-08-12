# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        current = dummy

        carry = 0

        while l1 or l2 or carry:

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry

            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next


def print_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


def main():
    solution = Solution()

    # Example 1:
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = solution.addTwoNumbers(l1, l2)
    print("Example 1:")
    print_list(result)

    # Example 2:
    l1 = ListNode(0)
    l2 = ListNode(0)
    result = solution.addTwoNumbers(l1, l2)
    print("Example 2:")
    print_list(result)

    # Example 3:
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    result = solution.addTwoNumbers(l1, l2)
    print("Example 3:")
    print_list(result)


if __name__ == "__main__":
    main()