
# 生成器 generator


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


if __name__ == '__main__':
    for x in fib(5):
        print(x)
