## Returning Boolian

import math

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,55,66,77,88,100]

def binary_search(numbers, value):
    lo = 0 
    hi = len(numbers)  

    while lo < hi: 
        m = math.floor(lo + (hi - lo)/2) 
        v = numbers[m]

        if v == value: 
            return True
        if v > value: 
            hi = m
        else: 
            lo = m + 1

    return False

res = binary_search(array, 78)
print(res)

## Returning the index 

import math

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,55,66,77,88,100]

def binary_search_index(numbers, value):
    lo = 0 
    hi = len(numbers)  

    while lo < hi: 
        m = math.floor(lo + (hi - lo)/2) 
        v = numbers[m]

        if v == value: 
            return m
        if v > value: 
            hi = m
        else: 
            lo = m + 1

    return -1

res = binary_search_index(array, 12)
print(res)
