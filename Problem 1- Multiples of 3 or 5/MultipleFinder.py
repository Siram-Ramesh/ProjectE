import numpy as np

# sum^(n/3)_(i=1)(3i) + sum^(n/5)_(i=1)(5i)  = 
#  3/2((n/3)^2 + n/3) + 5/2(n^2/25 + n/5)  =
#   n^2/6 + n + n^2/10 + n = 
#    (4/15)n^2 + 2n

def sumMultiples(max: int, factorList: list) -> int :
    factorArr = np.asarray(factorList)
    print("created factorArr ", factorArr)
    maxMultipleArr = np.floor((max-1)/factorArr)
    print("created maxMultipleArr ", maxMultipleArr)
    sumTermArr = factorArr * (((maxMultipleArr)**2) + (maxMultipleArr))/2
    print("created sumTermArr ", sumTermArr)
    return sumTermArr.sum()


print(sumMultiples(11, [3, 5]))