import numpy as np
import math

# we sum only evens AND fibonacci numbers, which means
# f_n = f_(n-1) + f_(n-2)
# f_(n-1) and f_(n-2) are either both even or both odd
# f_n ?= 2x + 2y
# f_n ?= 2x + 2y +2

def sumEvenFibonacci(maximum: int) -> int:
    if maximum < 2:
        return 0
    elif maximum == 2:
        return 2
    sum = 2
    fibList = [1, 2]
    n = 2
    fn = fibList[0] + fibList[1]
    while fn < maximum:
        if fn %2 == 0:
            sum += fn
        fibList.append(fn)
        fn = fibList[n] + fibList[n-1]
        n +=1
    return sum