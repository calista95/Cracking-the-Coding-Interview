#Program 4 Chapter 1 
#Name: Palindrome Permutation 
#Runtime: O(1)
#Date: 3/28/2019
#Notes:
'''
To implement a hash map in python,
1. initialize a table 
2. create a function to hash each key into a value 
3. insert into the table 
'''

#initialize hash table implementation 
table = [[] for _ in range(26)]

#hashes the key
def hashVal(key):
    return (ord(key.lower()))%97

#insert into table 
def insertTable(key,value):
    table[key].append(value)

#determines whether string is a palindrome permutation 
def isPermutation(str):
    for x in str: #put everything into a hash map 
        insertTable(hashVal(x),x)
    oddFlag = False
    for x in range(26):
        if len(table[x])%2!=0 and oddFlag == True: #if odd and there is already an odd
            return False
        elif len(table[x])%2!=0 and oddFlag == False:
            oddFlag=True    
    return True



#print(isPermutation("abba"))
#print(isPermutation("aboba"))
#print(isPermutation("abcbaa"))
print(isPermutation("Abba"))
#print (table)


