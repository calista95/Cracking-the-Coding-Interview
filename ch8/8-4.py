#Program: power set
#Write a method to return all subsets of a set 
#Method used: recursion
#Date: 4/10/2019


def all_subsets(given_array):
    #define an array size using arr size
    subset = [None]*len(given_array)
    helper(given_array,subset,0)
    #0 because we are starting with arr[0]

def print_set(subset):
    print(" ")
    for x in subset:
        print(x)
    print(" ")

def helper(given_array,subset,i):
    if i == len(given_array):
        print_set(subset)
    else:
        #first recursive call: we do not add the new element
        subset[i]=None
        helper(given_array,subset,i+1)
        #second recursive call: we add the new element
        subset[i]=given_array[i]
        helper(given_array,subset,i+1)

arr = [1,2,3]
all_subsets(arr)
