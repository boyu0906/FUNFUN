from test_framework import generic_test


def can_reach_end(A):
    farthest = 0
    for i in range(len(A)):
        farthest = max(farthest, i + A[i])
        if farthest >= len(A) - 1:  # this check must be before the next one
            return True
        if farthest <= i:
            return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
