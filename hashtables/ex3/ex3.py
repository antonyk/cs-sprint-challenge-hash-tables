def intersection(arrays):

    base_cache = {}

    # get shortest
    shortest = []
    if len(arrays) > 0:
        shortest = arrays[0]
    for _, v in enumerate(arrays):
        shortest = v if len(v) < len(shortest) else shortest

    # populate base cache, based on the shortest number list
    for num in shortest:
        base_cache[num] = None

    for _, v in enumerate(arrays):
        if v != shortest:
            new_cache = {}
            for num in v:
                if num in base_cache:
                    new_cache[num] = None
            
            base_cache = new_cache
            
    result = list(base_cache.keys())

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
