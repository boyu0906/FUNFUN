from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque


class QueueWithMax:
    def __init__(self):
        self._element, self._max_candidate = deque(), deque()

    def enqueue(self, x):
        self._element.append(x)
        if not self._max_candidate:
            self._max_candidate.append(x)
        else:
            while self._max_candidate:
                if self._max_candidate[-1] < x:
                    self._max_candidate.pop()
                else:
                    break
            self._max_candidate.append(x)

    def dequeue(self):
        if not self._element:
            raise IndexError('Empty queue')
        else:
            result = self._element.popleft()
            if result == self._max_candidate[0]:
                self._max_candidate.popleft()
        return result

    def max(self):
        if not self._element:
            raise IndexError('Empty queue')
        return self._max_candidate[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_with_max.py",
                                       'queue_with_max.tsv', queue_tester))
