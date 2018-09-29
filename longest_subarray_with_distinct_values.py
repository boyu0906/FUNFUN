from test_framework import generic_test


def longest_subarray_with_distinct_entries(A):

    d = {}
    n = len(A)
    max_length = 0
    '''
    i = 0
    while i < n:
        if A[i] not in d:
            d[A[i]] = i
        else:
            if len(d) > max_length:
                max_length = len(d)
            i = d[A[i]]
            d = {}
        i += 1
    return max(max_length, len(d))
    '''
    start_ind = 0
    for i, a in enumerate(A):
        if a in d:
            duplicate_ind = d[a]
            if duplicate_ind >= start_ind: # this condition is necessary!!!!!!
                max_length = max(max_length, i - start_ind)
                start_ind = duplicate_ind + 1
        d[a] = i
    return max(max_length, len(A) - start_ind)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
