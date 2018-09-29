from test_framework import generic_test


def parity(x):

    #result = 0
    #while x:
    #    result ^= 1
    #    x &= x-1
    #return result

    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
