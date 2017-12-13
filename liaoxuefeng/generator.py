
# 生成器 generator


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


def generator_function():
    for i in range(10):
        yield i


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    # for x in fib(5):
    #     print(x)
    # for item in generator_function():
    #     print(item)

    for x in fibon(6):
        print(x)

    my_string = 'Yasoob'
    my_iter = iter(my_string)
    print(next(my_iter))
    # >>>> 'Y'
