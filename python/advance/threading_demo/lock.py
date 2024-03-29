import threading
import time

# global variable
x = 0

def increment():
    global x
    x += 1

def thread_task(lock):
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()

def main_task():
    global x

    x = 0 # setting global variable x as 0

    # creating lock
    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    t1.start()
    t2.start()

    # t1.join()
    # t2.join()

if __name__ == '__main__':
    start_time = time.perf_counter()
    for i in range(10):
        main_task()
        print(f"iteration {i}: x = {x}")
    
    time_taken = time.perf_counter() - start_time
    print(time_taken)

