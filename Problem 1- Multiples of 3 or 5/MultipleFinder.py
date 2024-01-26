import numpy as np

# sum^(floor(n/3))_(i=1)(3i) + sum^(floor(n/5))_(i=1)(5i)  = 
#  3/2((floor(n/3))^2 + floor(n/3)) + 5/2((floor(floor(n/5))) + floor(n/5))  =

def sumMultiples(max: int, factorList: list) -> int :
    print("beginning sumMultiples for args", max, factorList)
    factorArr = np.asarray(factorList)
    print("created factorArr ", factorArr)
    maxMultipleArr = np.floor((max-1)/factorArr)
    print("created maxMultipleArr ", maxMultipleArr)
    sumTermArr = factorArr * (((maxMultipleArr)**2) + (maxMultipleArr))/2
    print("created sumTermArr ", sumTermArr)
    return sumTermArr.sum()