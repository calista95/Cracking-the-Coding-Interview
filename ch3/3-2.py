#Program 2 Chapter 3 
#Name: Stack Min
#Runtime: O(n)
#Date: 4/3/2019

import random

def push(val):
    arr.append(val)

def pop():
    return arr.pop()

def min():
    min = pop() #pop the first element 

    while((not arr) is False):
        temp = pop()
        print(str(temp))
        if (temp < min):
            min = temp
        
    return min
        

#initialize an array 
arr = []
for x in range(10):
    push(random.randint(1,10))

print("the min is: " + str(min()))