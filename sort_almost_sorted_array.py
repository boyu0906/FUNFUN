from test_framework import generic_test
import heapq


def sort_approximately_sorted_array(sequence, k):
    result = []
    min_heap = []
    for j in range(0, k):
        heapq.heappush(min_heap, next(sequence))
    while min_heap:
        result.append(heapq.heappop(min_heap))
        data = next(sequence, None)
        if data is not None:
            heapq.heappush(min_heap, data)
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
