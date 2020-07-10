def has_negatives(a):

    lookup = {}
    result = []
    for _, v in enumerate(a):
        if -v in lookup:
            result.append(abs(v))
        else:
            lookup[v] = None

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
