import collections
import functools
import math

from test_framework import generic_test
from test_framework.random_sequence_checker import run_func_with_retries
from test_framework.test_utils import enable_executor_hook


def nonuniform_random_number_generation(values, probabilities):
    import random, bisect, itertools

    # threshold = [0] * len(probabilities)
    # threshold[0] = probabilities[0]
    # for i in range(1, len(probabilities)):
    #     threshold[i] = threshold[i - 1] + probabilities[i]

    threshold = list(itertools.accumulate(probabilities))
    rand_value = random.random()  # random.uniform(0, 1)
    idx = bisect.bisect(threshold, rand_value)
    return values[idx]


@enable_executor_hook
def nonuniform_random_number_generation_wrapper(executor, values,
                                                probabilities):
    def nonuniform_random_number_generation_runner(executor, values,
                                                   probabilities):
        N = 10**6
        result = executor.run(lambda : [nonuniform_random_number_generation(values, probabilities) for _ in range(N)])

        counts = collections.Counter(result)
        for v, p in zip(values, probabilities):
            if N * p < 50 or N * (1.0 - p) < 50:
                continue
            sigma = math.sqrt(N * p * (1.0 - p))
            if abs(float(counts[v]) - (p * N)) > 5 * sigma:
                return False
        return True

    run_func_with_retries(
        functools.partial(nonuniform_random_number_generation_runner, executor,
                          values, probabilities))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "nonuniform_random_number.py", 'nonuniform_random_number.tsv',
            nonuniform_random_number_generation_wrapper))
