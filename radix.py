import random
import time
import math

unsorted_list = [random.randint(0, 10000000) for i in range(10000000)]

def radix(list):
    
    sorted_list = list
    position = 1

    while position < 999:
        tempTable = [[] for i in range(10)]
        

        for item in sorted_list: 
            tempTable[int((item / position)) % 10].append(item)

        sorted_list = []

        for item in tempTable:

            sorted_list += item
            # if item is None:
            #     continue

            # for i in item:
            #     sorted_list.append(i)
        
        
                
        position *= 10
    return sorted_list


start = time.time()
radix(unsorted_list)
end = time.time()

print((end - start))


start = time.time()
unsorted_list.sort()
end = time.time()

print((end - start))