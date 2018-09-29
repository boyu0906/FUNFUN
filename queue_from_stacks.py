from test_framework import generic_test


class Queue:
    def __init__(self):
        self._stack1 = []  # used to enqueue
        self._stack2 = []  # used to dequeue

    def enqueue(self, x):
        self._stack1.append(x)

    def dequeue(self):
        if not self._stack2:
            if not self._stack1:
                raise IndexError('Empty queue')
            else:
                while self._stack1:
                    self._stack2.append(self._stack1.pop())
        return self._stack2.pop()


def queue_tester(ops):
    from test_framework.test_failure import TestFailure

    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_from_stacks.py",
                                       'queue_from_stacks.tsv', queue_tester))
