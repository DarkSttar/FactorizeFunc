from multiprocessing import Pool,cpu_count
import os
from time import time
def factorize(number):
    results = []
    factors = []
    divisor = 1
    while divisor < number / divisor:
        if  number % divisor == 0:
            factors.append(int(divisor))
            factors.append(int(number / divisor))    
        
        divisor += 1
    factors.sort()
    results.append(factors)
    return results





def factorize_sync(*numbers):
    results = []
    
    for number in numbers:
        factors = []
        divisor = 1
        while divisor < number / divisor:
            if  number % divisor == 0:
                factors.append(int(divisor))
                factors.append(int(number / divisor))    
            
            divisor += 1
        factors.sort()
        results.append(factors)
    return results




def factorize_parallel(*numbers):
    with Pool(cpu_count()) as p:
        return [item[0] for item in p.map(factorize,numbers)]
      
        
if __name__ == "__main__":
    start_time = time()
    a,b,c,d = factorize_parallel(128, 255, 99999, 10651060)
    end_time = time()
    total_time = end_time - start_time
    print(f'Use factorize_parallel: TOTAL TIME ==> {total_time}')
    start_time = time()
    a_sync,b_sync,c_sync,d_sync = factorize_sync(128, 255, 99999, 10651060)
    end_time = time()
    total_time = end_time - start_time
    print(f'Use factorize_sync: TOTAL TIME ==> {total_time}')
    
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    assert a_sync == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b_sync == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c_sync == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d_sync == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]