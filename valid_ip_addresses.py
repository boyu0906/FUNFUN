from test_framework import generic_test


def get_valid_ip_address(s):

    def is_valid_part(t):  # check invalid cases
        return (len(t) == 1) or (t[0] != '0' and int(t) < 256)

    address = []
    for i in range(min(3, len(s))):
        one_address = [''] * 4
        if is_valid_part(s[0: i + 1]):
            one_address[0] = s[0: i + 1]
            for j in range(i + 1, min(i + 4, len(s))):
                if is_valid_part(s[i + 1: j + 1]):
                    one_address[1] = s[i + 1: j + 1]
                    for k in range(j + 1, min(j + 4, len(s) - 1)):
                        if is_valid_part(s[j + 1: k + 1]) and is_valid_part(s[k + 1: len(s)]):
                            one_address[2] = s[j + 1: k + 1]
                            one_address[3] = s[k + 1: len(s)]
                            address.append('.'.join(one_address))

    return address


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            'valid_ip_addresses.tsv',
            get_valid_ip_address,
            comparator=comp))
