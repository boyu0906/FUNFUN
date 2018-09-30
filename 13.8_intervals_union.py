import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals):

    intervals.sort(key=lambda e: (e.left.val, not e.left.is_closed))
    result, temp_interval = [], intervals[0]
    for interval in intervals:
        if (interval.left.val <= temp_interval.right.val) and \
                not (interval.left.val == temp_interval.right.val and
                     interval.left.is_closed == temp_interval.right.is_closed == False):
            temp_interval = Interval(min(temp_interval.left, interval.left, key=lambda e:(e.val, not e.is_closed)),
                                     max(temp_interval.right, interval.right, key=lambda e:(e.val, e.is_closed)))
        else:
            result.append(temp_interval)
            temp_interval = interval
    result.append(temp_interval) # don't forget the last step!!!
    return result


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intervals_union.py",
                                       "intervals_union.tsv",
                                       union_of_intervals_wrapper))
