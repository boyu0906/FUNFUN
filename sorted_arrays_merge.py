from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    for i, x in enumerate(sorted_arrays_iters):
        first_element = next(x, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        small_element, small_ind = heapq.heappop(min_heap)
        result.append(small_element)
        small_array_iter = sorted_arrays_iters[small_ind]
        first_element = next(small_array_iter, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, small_ind))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
