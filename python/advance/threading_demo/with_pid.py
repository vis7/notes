import os
import threading

def task1():
    print(f'task1 is assigned to thread: {threading.current_thread().name}')
    print(f'ID of process running task1: {os.getpid()}')

def task2():
    print(f'task2 is assigned to thread: {threading.current_thread().name}')
    print(f'ID of process running task2: {os.getpid()}')

if __name__ == '__main__':
    print(f'main function is assigned to thread: {threading.current_thread().name}')
    print(f'ID of process running main: {os.getpid()}')

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    t1.start()
    t2.start()

    # t1.join()
    # t2.join()
