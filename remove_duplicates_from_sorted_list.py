from test_framework import generic_test


def remove_duplicates(L):
    l0 = l1 = L
    while l0:
        l0 = l0.next
        while l0 and l0.data == l1.data:
            l0 = l0.next
        l1.next = l0
        l1 = l1.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
