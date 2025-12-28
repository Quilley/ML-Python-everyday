# Given an array of integers nums and an integer k, return the sliding window mean at that index of the subarray with length k
from typing import List

def windows(numbers: List[int], k: int):
    sum = 0
    final = []

    if len(numbers)<k:
        return []  



    for ind, val in enumerate(numbers):
        # print(ind)
        if ind > (k-1):
            # print(ind)
            sum =0
            for j in range(ind+1-k,ind+1):
                print(j)
                sum += numbers[j]
            
            
            final.append(sum/k)

        
    
    return final

test1= [1,23, 3, 5,8, 10]

print(windows(test1, 3))

