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
