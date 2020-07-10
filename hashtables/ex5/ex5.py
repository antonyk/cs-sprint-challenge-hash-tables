# Your code here

def finder(files, queries):

    lookup = {}
    for _, v in enumerate(files):
        f = v.split('/')
        if f[-1] in lookup:
            lookup[f[-1]].append(v)
        else:
            lookup[f[-1]] = [v]

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
