import asyncio
# 协程


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print(f'[CONSUMER] Consuming {n}...')
        r = '200 OK'


def produce(c):
    c.send(None)

    n = 0
    while n < 5:
        n += 1
        print(f'[PRODUCER] Producing {n}..')

        r = c.send(n)

        print(f'[PRODUCER] Consumer return {r}')
    c.close()


#########################################################

@asyncio.coroutine
def hello():
    print('Hello World')
    r = yield from asyncio.sleep(1)
    print('Hello again')


if __name__ == '__main__':
    # 生产者消费者模型
    # c = consumer()
    # produce(c)
    #####################################
    # asyncioxie 
    # 获取event_loop
    loop = asyncio.get_event_loop()
    # 把协程丢进loop中执行
    loop.run_until_complete(hello())
    loop.close()
