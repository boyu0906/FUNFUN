from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    ind1, ind2 = 0, 0
    #previous = float('inf')
    result = []
    while ind1 < len(A) and ind2 < len(B):
        if A[ind1] < B[ind2]:
            ind1 += 1
        elif A[ind1] > B[ind2]:
            ind2 += 1
        else:
            #if A[ind1] != previous:
            if ind1 == 0 or A[ind1] != A[ind1 - 1]:
                result.append(A[ind1])
                #previous = A[ind1]
            ind1 += 1
            ind2 += 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
