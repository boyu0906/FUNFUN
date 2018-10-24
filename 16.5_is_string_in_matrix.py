from test_framework import generic_test


def is_pattern_contained_in_grid(grid, S):
    def helper(candidate, k):
        if k == len(S):
            return True
        for i, j in candidate:
            if grid[i][j] == S[k] and (i, j, k) not in previous_attempts:
                new_candidate = []
                if i - 1 >= 0:
                    new_candidate.append((i - 1, j))
                if i + 1 < len(grid):
                    new_candidate.append((i + 1, j))
                if j - 1 >= 0:
                    new_candidate.append((i, j - 1))
                if j + 1 < len(grid[0]):
                    new_candidate.append((i, j + 1))
                result = helper(new_candidate, k + 1)
                if result:
                    return True
            else:
                previous_attempts.add((i, j, k))
        return False
    previous_attempts = set()
    initial_candidate = [(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]
    return helper(initial_candidate, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
