
def get_indices_of_item_weights(weights, length, limit):

    lookup = {}
    for i, v in enumerate(weights):
        diff = limit - v
        if diff in lookup:
            return (i, lookup[diff])
        else:
            lookup[v] = i


    return None
