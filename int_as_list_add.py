from test_framework import generic_test
from list_node import ListNode


def add_two_numbers(L1, L2):
    carrier = 0
    L3 = L3_head = ListNode(0)
    while L1 or L2:
        a = L1.data if L1 else 0
        b = L2.data if L2 else 0
        sum = a + b + carrier
        L3.next = ListNode(sum % 10)
        L3 = L3.next
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        carrier = sum // 10
    # don't forget to add the final carrier out bit!!!!!
    if carrier == 1:
        L3.next = ListNode(1)
    return L3_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
