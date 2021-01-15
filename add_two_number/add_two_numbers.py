class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print("inside addTwoNumbers")

        # set dummy and cur variable to equal new ListNode
        dummy = cur = ListNode(0)
        carry = 0

        # while l1 or l2 or carry exists
        while l1 or l2 or carry:
            # add l1 and l2 val to carry, set new l1 and l2
            if l1:
                carry = carry + l1.val
                l1 = l1.next
            if l2:
                carry = carry + l2.val
                l2 = l2.next
            # create next node, with value of carry mod 10
            # to get the least significant digit
            cur.next = ListNode(carry % 10)
            cur = cur.next
            # floor divide carry by 10
            # to get the most significant digit (1 if > 10)
            carry = carry // 10
        return dummy.next


def convert_to_ListNode(n):
    previous_node = None
    first = None
    for digit in str(n):
        current_node = ListNode(int(digit))
        if first is None:
            first = current_node
        if previous_node is not None:
            previous_node.next = current_node
        previous_node = current_node
    return first


def main():
    list_node_test = convert_to_ListNode(123)
    while list_node_test is not None:
        print(list_node_test.val)
        list_node_test = list_node_test.next
    # 1 -> 2 -> 6
    l1 = convert_to_ListNode(621)

    # 4 -> 5 -> 6
    l2 = convert_to_ListNode(654)

    # 5 -> 7 -> 9
    l_actual = convert_to_ListNode(975)

    sol = Solution()
    # 456 + 126 = 582
    l_sol = sol.addTwoNumbers(l1, l2)

    while l_sol is not None:
        print(l_sol.val)
        l_sol = l_sol.next

    try:
        assert l_sol == l9
    except:
        print("Test failed")


if __name__ == "__main__":
    main()