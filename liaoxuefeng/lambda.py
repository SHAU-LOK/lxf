

if __name__ == '__main__':

    def add(x, y): return x + y
    print(add(3, 5))
    # >>>>>> 8

    a = [(1, 2), (4, 1), (8, 10), (13, -3)]
    a.sort(key=lambda x: x[1])
    print(a)
    # >>>>>>>[(13, -3), (4, 1), (1, 2), (8, 10)]

    list1 = [3, 5, 36, 67, -1]
    list2 = [3, 2, 304, -24, 55]
    data = zip(list1, list2)
    data = sorted(data)
    print(data)
    list1, list2 = map(lambda t: list(t), zip(*data))
    print(list1)
    print(list2)
    # >>> [(-1, 55), (3, 3), (5, 2), (36, 304), (67, -24)]
    # >>> [-1, 3, 5, 36, 67]
    # >>> [55, 3, 2, 304, -24]

    # print(list(zip(*data)))
    print(*data)
