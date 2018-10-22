from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    # DP
    num_combinations_for_score = [[1] + [0] * final_score for _ in individual_play_scores]
    for i in range(len(individual_play_scores)):  # for each row
        for j in range(1, final_score + 1):  # for each final score
            with_out_this_play = (num_combinations_for_score[i - 1][j]
                                  if i >= 1 else 0)
            with_this_play = (num_combinations_for_score[i][j - individual_play_scores[i]]
                              if j >= individual_play_scores[i] else 0)
            num_combinations_for_score[i][j] = with_out_this_play + with_this_play
    return num_combinations_for_score[-1][-1]

    # backtracking
    # def helper(target, ind):
    #     total = 0
    #     if target == 0:
    #         return 1
    #     for i in range(ind, len(individual_play_scores)):
    #         if individual_play_scores[i] > target:  # to break early
    #             break
    #         total += helper(target - individual_play_scores[i], i)
    #     return total
    # individual_play_scores.sort()
    # return helper(final_score, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
