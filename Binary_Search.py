#Binary search
import time
import random

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low = None, high = None):

    if low == None:
        low = 0
    if high == None:
        high = len(l)-1

    if high < low:
        return -1

    midpoint = (low + high)//2

    if (l[midpoint] == target):
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)


if __name__ == '__main__':
    length = 100000
    l = set()
    while len(l) < length:
        l.add(random.randint(-3*length, 3*length))
    l = sorted(list(l))
    #l = [1,3,5,10,12,24,5,0,34,56,75,43,45,98,78,6,7,54,999]
    target = 999

    print("NAIVE_SEARCH : ")
    start_time = time.time()
    print(naive_search(l,target))
    print("Time taken : ", time.time() - start_time)
    print("\n\nBINARY_SEARCH : ")
    start_time = time.time()
    print(binary_search(l,target))
    print("Time taken : ",time.time() - start_time)
