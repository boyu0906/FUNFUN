import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals, new_interval):
    result = []
    L, R = new_interval.left, new_interval.right
    i = 0
    while (i < len(disjoint_intervals) and disjoint_intervals[i].right < new_interval.left):
        result.append(disjoint_intervals[i])
        i += 1
    while (i < len(disjoint_intervals) and disjoint_intervals[i].left <= new_interval.right):
        new_interval = Interval(min(disjoint_intervals[i].left, new_interval.left),
                                max(disjoint_intervals[i].right, new_interval.right))
        i += 1
    return result + [new_interval] + disjoint_intervals[i:]
    '''
    flag = 0
    for ind in range(len(disjoint_intervals)):
        interval = disjoint_intervals[ind]
        if flag == 1: # done with interval merge
            result.append(interval)
            continue
        if L < interval.left:
            if R < interval.left:
                result.append(Interval(L, R))
                flag = 1
                result.append(interval)
            elif interval.left <= R <= interval.right:
                result.append(Interval(L, interval.right))
                flag = 1
            else:
                if ind == len(disjoint_intervals) - 1:
                    result.append(Interval(L, R))
        elif interval.left <= L <= interval.right:
            if R < interval.right:
                result.append(interval)
                flag = 1
            else:
                L = interval.left
                if ind == len(disjoint_intervals) - 1:
                    result.append(Interval(L, R))
        else:
            result.append(interval)
            if ind == len(disjoint_intervals) - 1:
                result.append(Interval(L, R))
    '''
    return result


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            'interval_add.tsv',
            add_interval_wrapper,
            res_printer=res_printer))
