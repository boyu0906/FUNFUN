from test_framework import generic_test


def shortest_equivalent_path(path):
    if not path:
        raise ValueError('Invalid path')
    result = []
    if path[0] == '/':
        result.append('/')
    for token in (token for token in path.split('/') if token not in ['', '.']):
        if token == '..':
            if not result or result[-1] == '..':    ## '../../a/b/c'
                result.append(token)
            else:
                if result[-1] == '/':               ## '/a/../../../b'
                    raise ValueError('Invalid path')
                else:
                    result.pop()
        else:
            result.append(token)
    final_path = '/'.join(result)
    return final_path[final_path.startswith('//'):]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
