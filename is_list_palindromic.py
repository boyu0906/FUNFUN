from test_framework import generic_test


def is_linked_list_a_palindrome(L):
    def reverse_linked_list(head):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre

    # find the second half of L (good for both even and odd length)
    fast = slow = L
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    first_half_iter, second_half_iter = L, reverse_linked_list(slow)
    while first_half_iter and second_half_iter:
        if first_half_iter.data != second_half_iter.data:
            return False
        first_half_iter, second_half_iter = first_half_iter.next, second_half_iter.next
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
