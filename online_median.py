from test_framework import generic_test
import heapq


def online_median(sequence):
    left_heap, right_heap, result = [], [], []
    for x in sequence:
        heapq.heappush(left_heap, -heapq.heappushpop(right_heap, x))
        if len(right_heap) < len(left_heap):
            heapq.heappush(right_heap, -heapq.heappop(left_heap))

        if len(right_heap) == len(left_heap):
            result.append((-left_heap[0] + right_heap[0])/2)
        else:
            result.append(right_heap[0])

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
