import numpy as np
import math

# sum^(floor(n/3))_(i=1)(3i) + sum^(floor(n/5))_(i=1)(5i)  = 
#  3/2((floor(n/3))^2 + floor(n/3)) + 5/2((floor(floor(n/5))) + floor(n/5))  =

def sumMultiples(max: int, factorList: list) -> int :
    print("beginning sumMultiples for args", max, factorList)
    if len(factorList) > 2:
        print("Please limit size of factorList to 2") 
        return -1
    factorArr = np.asarray(factorList)
    print("created factorArr ", factorArr)
    maxMultipleArr = np.floor((max-1)/factorArr)
    print("created maxMultipleArr ", maxMultipleArr)
    sumTermArr = factorArr * (((maxMultipleArr)**2) + (maxMultipleArr))/2
    print("created sumTermArr ", sumTermArr)
    
    excludeFactor = factorList[0]*factorList[1]
    print("created excludeFactor: ", excludeFactor)
    excludeMaxMultiple = math.floor((max-1)/excludeFactor)
    excludeTerm = excludeFactor * ((excludeMaxMultiple**2) + (excludeMaxMultiple))/2
    print("final excludeTerm ", excludeTerm)

    return sumTermArr.sum() - excludeTerm