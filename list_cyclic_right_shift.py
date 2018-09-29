from test_framework import generic_test


def cyclically_right_shift_list(L, k):
    if not L:
        return L     # corner case !!!

    l0 = l1 = l2 = L
    n = 1
    while l2.next:
        n += 1
        l2 = l2.next

    k %= n
    if k == 0:  # another special case !!!
        return L

    for _ in range(k):
        l1 = l1.next
    while l1.next:
        l0, l1 = l0.next, l1.next
    new_head = l0.next
    l0.next = None
    l1.next = L
    return new_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
