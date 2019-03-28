#Program 2 Chapter 1 
#Name: Check Permutation
#Runtime: the built-in sorting algorithm of Python 
# uses a special version of merge sort, called Timsort, which runs in nlog2n time
#Date: 3/28/2019
#Note: In an actual interview, ask if whitespace and case sensitivity counts 

def permutation(a, b):
    if len(a) != len(b): #if the two strings are already of different lengths, they cannot be a permutation 
        return False
    a = sorted(a)
    b = sorted(b)
    if a == b:
        return True
    return False

print(permutation("zxcadf","asfseg"))
print(permutation("cat","atc"))
print(permutation("meow","wome"))