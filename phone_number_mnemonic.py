from test_framework import generic_test, test_utils

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')


def phone_mnemonic(phone_number):

    result, one_result = [], [0] * len(phone_number)

    def phone_mnemonic_helper(k):
        if k == len(phone_number):
            result.append(''.join(one_result))
        else:
            for c in MAPPING[int(phone_number[k])]:
                one_result[k] = c
                phone_mnemonic_helper(k + 1)

    phone_mnemonic_helper(0)

    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
