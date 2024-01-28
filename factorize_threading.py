from threading import Thread, Semaphore
from time import time
semaphore = Semaphore()
results = []

def factorize(number):
    semaphore.acquire()    
    factors = []
    divisor = 1
    while divisor < number / divisor:
        if number % divisor == 0:
            factors.append(int(divisor))
            factors.append(int(number / divisor))    
        
        divisor += 1
    factors.sort()
    semaphore.release()
    results.append(factors)

def factorize_thread(*numbers):
    global results
    threads = []
    for number in numbers:
        thread = Thread(target=factorize, args=(number,))
        threads.append(thread)
        thread.start()

    for th in threads:
        th.join()

    return results

if __name__ == "__main__":
    start_time = time()
    a,b,c,d = factorize_thread(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    end_time = time()
    total_time = end_time - start_time
    print(f'Use thread: TOTAL TIME ==> {total_time}')