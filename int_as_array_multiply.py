from test_framework import generic_test


def multiply(num1, num2):
    result = [0] * (len(num1) + len(num2))
    sign = 2 * (num1[0] * num2[0] >= 0) - 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    for ind2 in reversed(range(len(num2))):
        for ind1 in reversed(range(len(num1))):
            temp = num1[ind1] * num2[ind2]
            result[ind1 + ind2 + 1] += temp
            #result[ind1 + ind2] += temp // 10  # Wrong!!!
            result[ind1 + ind2] += result[ind1 + ind2 + 1] // 10
            result[ind1 + ind2 + 1] %= 10
    # remove the leading zeros (corner case: all zeros)
    #while result[0] == 0:
    #    result = result[1:]
    #    if len(result) == 1:
    #        break
    result = result[next( (i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    result = [sign * result[0]] + result[1:]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
