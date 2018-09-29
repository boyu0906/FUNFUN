from test_framework import generic_test, test_utils
import heapq


def k_largest_in_binary_heap(A, k):
    #return heapq.nlargest(k, A)
    if k <= 0:
        return []
    candidate_heap, result = [], []
    heapq.heappush(candidate_heap, (-A[0], 0))
    for _ in range(k):
        max_candidate = heapq.heappop(candidate_heap)
        result.append(-max_candidate[0])
        left_index = max_candidate[1] * 2 + 1
        right_index = max_candidate[1] * 2 + 2
        if left_index < len(A):
            heapq.heappush(candidate_heap, (-A[left_index], left_index))
        if right_index < len(A):
            heapq.heappush(candidate_heap, (-A[right_index], right_index))
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
