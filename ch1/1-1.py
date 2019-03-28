#Program 1 Chapter 1 
#Name: Is Unique
#Runtime: O(n^2)
#Date: 3/28/2019

def isUniqueChars(mystr):
    if len(mystr) > 128:
        return False
    for x in range(len(mystr)):
        for y in range(len(mystr)):
            if (x != y): #do not compare the same indices 
                if mystr[x] == mystr[y]:
                    return False
    return True


result = isUniqueChars("abc")
print(str(result))

result = isUniqueChars("aba")
print(str(result))

result = isUniqueChars("abcaaaaaa")
print(str(result))
