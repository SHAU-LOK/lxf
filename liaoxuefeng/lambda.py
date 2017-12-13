
from functools import reduce


def inc(x):
    def incx(y):
        return x + y
    return incx


inc2 = inc(2)
inc5 = inc(5)


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

    print(inc2(5))
    # >>> 7
    print(inc5(5))
    # >>> 10

    name_len = map(len, ['hao', 'cheng', 'coooksdd'])
    print(list(name_len))
    # >>>> [3, 5, 8]

    print(list(map(lambda x: x.upper(),  ['hao', 'cheng', 'coooksdd'])))
    # >>> ['HAO', 'CHENG', 'COOOKSDD']

    print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
    # >>> 15

    # 1）找出偶数。
    # 2）乘以3
    # 3）转成字符串返回

    def even_filter(nums):
        return filter(lambda x: x % 2 == 0, nums)

    def multiply_by_three(nums):
        return map(lambda x: x * 3, nums)

    def convert_2_str(nums):
        return map(lambda x: str(x), nums)

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
