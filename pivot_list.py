import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from list_node import ListNode


def list_pivoting(l, x):
    l1 = l1_head = ListNode(0)
    l2 = l2_head = ListNode(0)
    l3 = l3_head = ListNode(0)

    while l:
        if l.data < x:
            l1.next = l
            l1 = l1.next
        elif l.data == x:
            l2.next = l
            l2 = l2.next
        else:
            l3.next = l
            l3 = l3.next
        l = l.next

    # combine the three lists, it is possible some lists are empty!!!
    l1.next = l2_head.next
    l2.next = l3_head.next
    l3.next = None
    if l1_head.next:
        if l2_head.next:
            l1.next = l2_head.next
            if l3_head.next:
                l2.next = l3_head.next
                l3.next = None
            else:
                l2.next = None
        else:
            if l3_head.next:
                l1.next = l3_head.next
                l3.next = None
            else:
                l1.next = None
        return l1_head.next
    else:
        if l2_head.next:
            if l3_head.next:
                l2.next = l3_head.next
                l3.next = None
            else:
                l2.next = None
            return l2_head.next
        else:
            if l3_head.next:
                l3.next = None
                return l3_head.next
            else:
                return None


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pivot_list.py", 'pivot_list.tsv',
                                       list_pivoting_wrapper))
