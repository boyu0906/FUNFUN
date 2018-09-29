import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from is_list_cyclic import has_cycle
from do_terminated_lists_overlap import overlapping_no_cycle_lists


def overlapping_lists(l0, l1):
    root0, root1 = has_cycle(l0), has_cycle(l1)
    if not root0 and not root1:
        return overlapping_no_cycle_lists(l0, l1)
    elif (not root0 and root1) or (root0 and not root1):
        return None
    # both lists have cycles: (1) disjoint cycles (2) starting nodes in cycles are the same
    # (3) starting nodes in cycles are different
    temp = root1
    while True:
        temp = temp.next
        if temp is root0 or temp is root1:
            break
    if temp is not root0:
        return None  # disjoint cycles

    def distance(s, t):
        dist = 0
        while s is not t:
            dist += 1
            s = s.next
        return dist

    length0, length1 = distance(l0, root0), distance(l1, root1)
    if length0 > length1:
        l0, l1 = l1, l0
        root0, root1 = root1, root0
    for i in range(abs(length0 - length1)):
        l1 = l1.next
    while l0 is not l1 and l0 is not root0 and l1 is not root1:
        l0, l1 = l0.next, l1.next
    return l0 if l0 is l1 else root0


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_lists_overlap.py",
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
