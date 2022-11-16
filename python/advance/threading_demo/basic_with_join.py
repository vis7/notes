import threading

def square_number(num):
    print(f'square of number: {num*num}')

def cube_number(num):
    print(f'cube of number: {num*num*num}')

if __name__ == '__main__':
    t1 = threading.Thread(target=square_number, args=(10,))
    t2 = threading.Thread(target=cube_number, args=(10,))

    t1.start()
    t2.start()

    # t1.join()
    # t2.join()

    print('Done!')

