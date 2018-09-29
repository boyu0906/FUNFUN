from test_framework import generic_test


def next_permutation(perm):
    '''
    L = len(perm)
    if L == 1:
        return []
    cnt = 0
    for i in reversed(range(1, len(perm))):
        if perm[i-1] < perm[i]:
            break
        cnt += 1
    if cnt == L - 1:
        return []
    else:
        p1 = perm[0: i - 1]
        p2 = perm[i:]
        s = min(x for x in p2 if x > perm[i - 1])
        p2.append(perm[i - 1])
        p2.remove(s)
        perm[i - 1] = s
        perm = p1 + [perm[i - 1]] + sorted(p2)
        return perm
    '''
    switch_point = len(perm) - 2
    while switch_point >= 0 and perm[switch_point] >= perm[switch_point + 1]:
        switch_point -= 1
    if switch_point < 0:
        return []
    #print('switch_point = ', switch_point)
    for i in reversed(range(switch_point + 1, len(perm))):
        if perm[i] > perm[switch_point]:
            perm[i], perm[switch_point] = perm[switch_point], perm[i]
            break
    #print(perm)
    return perm[0:switch_point + 1] + list(reversed(perm[switch_point + 1 :]))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))
