import numpy as np

# sum^(n/3)_(i=1)(3i) + sum^(n/5)_(i=1)(5i)  = 
#  3/2(n^2/9 + n/3) + 5/2(n^2/25 + n/5)  =
#   n^2/6 + n + n^2/10 + n = 
#    (4/15)n^2 + 2n

def sumMultiples(max: int, factorList: list) -> int :
    factorArr = np.asarray(factorList)
    sumTermArr = ((max^2)/factorArr)/2 +  max
    return sumTermArr.sum()
