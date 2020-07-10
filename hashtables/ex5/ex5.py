# Your code here

def finder(files, queries):

    lookup = {}
    for _, v in enumerate(files):
        # v1
        f = v.split('/')
        if f[-1] in lookup:
            lookup[f[-1]].append(v)
        else:
            lookup[f[-1]] = [v]

        # v2
        # f = v.split('/')
        # found = lookup.get(f[-1])
        # if found:
        #     lookup[f[-1]].append(v)
        # else:
        #     lookup[f[-1]] = [v]

        # v3
        # idx = v.rfind('/')
        # f = ''
        # if idx > -1:
        #     f = v[idx+1:]
        # if f in lookup:
        #     lookup[f].append(v)
        # else:
        #     lookup[f] = [v]

    result = []
    for _, v in enumerate(queries):
        if v in lookup:
            result.extend(lookup[v])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
