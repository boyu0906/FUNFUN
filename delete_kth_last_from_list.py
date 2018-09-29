from test_framework import generic_test
from list_node import ListNode


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    dummy_head = ListNode(0, L)
    l0, l1 = dummy_head.next, dummy_head
    for i in range(k):
        l0 = l0.next

    while l0:
        l0, l1 = l0.next, l1.next
    l1.next = l1.next.next
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
