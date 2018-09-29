from test_framework import generic_test


def even_odd_merge(L):
    if not L:
        return L
    even, odd, odd_head = L, L.next, L.next

    '''
    # cannot update even and odd separately
    while even and even.next and even.next.next:  
        even.next = even.next.next
        even = even.next
    while odd and odd.next and odd.next.next:
        odd.next = odd.next.next
        odd = odd.next
    '''
    while even and even.next and even.next.next:
        even.next = even.next.next
        even = even.next
        odd.next = odd.next.next
        odd = odd.next

    even.next = odd_head

    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
