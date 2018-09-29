import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))
Endpoint = collections.namedtuple('Endpoint', ('value', 'isStart'))


def find_max_simultaneous_events(A):
    # A has already been converted into namedtupe Event in the wrapper
    endpoints = [p for a in A for p in [Endpoint(a.start, True), Endpoint(a.finish, False)]]
    endpoints.sort(key=lambda x: (x.value, not x.isStart)) # breaking ties by putting start times before end times
    max_num_events, num_events = 0, 0
    for x in endpoints:
        if x.isStart:
            num_events += 1
            max_num_events = max(max_num_events, num_events)
        else:
            num_events -= 1
        #max_num_events = max(max_num_events, num_events)
    return max_num_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
