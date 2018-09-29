from test_framework import generic_test


def find_all_substrings(s, words):
    result = []

    n, m = len(words[0]), len(words)
    for start_ind in range(len(s) - n*m + 1): # one improvement here is the minus n*m
        temp = s[start_ind:start_ind+n]
        cnt, ind = 0, start_ind
        word_list = list(words)
        while temp in word_list:
            cnt += 1
            word_list.remove(temp)
            if cnt == m:
                result.append(start_ind)
                break
            else:
                ind += n
                temp = s[ind:ind + n]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "string_decompositions_into_dictionary_words.py",
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
