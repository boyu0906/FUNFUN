from test_framework import generic_test
from collections import namedtuple


def examine_buildings_with_sunset(sequence):
    BuildingWithHeight = namedtuple('BuildingWithHeight', ('id','height'))
    result = []
    for (i, h) in enumerate(sequence):
        '''
        if not result:
            result.append(BuildingWithHeight(i, h))
        else:
            while result and h >= result[-1].height:
                result.pop()
            result.append(BuildingWithHeight(i, h))
        '''
        while result and h >= result[-1].height:
            result.pop()
        result.append(BuildingWithHeight(i, h))
    return [c.id for c in reversed(result)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
