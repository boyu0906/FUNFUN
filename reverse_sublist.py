from test_framework import generic_test
from list_node import ListNode


def reverse_sublist(L, start, finish):
    sublist_head = dummy_head = ListNode(0, L)
    for i in range(1, start):
        sublist_head = sublist_head.next

    current = sublist_head.next
    for i in range(finish - start):
        post = current.next
        current.next = post.next
        post.next = sublist_head.next
        sublist_head.next = post

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
