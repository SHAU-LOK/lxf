
from threading import Thread
import time


def my_counter():
    i = 0
    for _ in range(100000000):
        i += 1
    return True


if __name__ == '__main__':
    
    # 顺序执行单线程
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        t.join()
    end_time = time.time()
    print(f'顺序执行单线程 Total time:{end_time - start_time}')


    # 同时执行的两个并发线程

    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        thread_array[tid] = t
    
    for i in range(2):
        thread_array[i].join()

    end_time = time.time()
    print(f'顺序执行多线程 Total time:{end_time - start_time}')


