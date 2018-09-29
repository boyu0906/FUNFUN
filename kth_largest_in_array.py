from test_framework import generic_test
import random


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    # memory issue
    left, right = [], []
    rand_indx = 0  #random.randint(0, len(A)-1)
    temp = A[rand_indx]
    #print('k:', k)
    #print('A:', A)
    for x in A[1:]:
        if x <= A[rand_indx]:
            left.append(x)
        elif x > A[rand_indx]:
            right.append(x)
    #print('left length:', len(left))
    #print('left:', left)
    #print('right length:', len(right))
    #print('right', right)
    if len(right) == k - 1:
        return temp
    elif len(right) < k - 1:
        return find_kth_largest(k - len(right)-1, left)
    else:
        return find_kth_largest(k, right)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
