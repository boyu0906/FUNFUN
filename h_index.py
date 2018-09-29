from test_framework import generic_test


def h_index(citations):
    citations.sort()
    n = len(citations)
    result = 0
    for i, x in enumerate(citations):
        '''
        if x < n - i:
            result = x
        else:
            result = n - i
            break
        '''
        if x >= n - i:
            return n - i
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main("h_index.py", 'h_index.tsv', h_index))
