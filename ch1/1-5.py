#Program 5 Chapter 1 
#Name: One Away 
#Runtime: O(n)
#Date: 4/1/2019
#Notes: The removed letter may not be duplicated in a row. For example, bye and byee will not work, since you can remove either one of the e's. 
#However, it will work if they are separated by at least one other char, like bye and beye.

def oneAway(str1, str2):
    if (len(str1) == len(str2)):
        return replace(str1, str2)
    elif (len(str1)+1 == len(str2)): #str2 is longer by 1 
        return switchOne(str1, str2)
    elif (len(str2)+1 == len(str1)): #str1 is longer by 1 
        return switchOne(str2, str1)
    else:
        return False

#return true if there is a one char difference between the two strings 
def replace(str1, str2):
    diff=0 #keep track of the number of differences 
    for x in range(len(str1)):
        if (str1[x] != str2[x]):
            diff+=1
    if diff >=2:
        return False
    else:
        return True
    
#return true if you can take one letter out of str2 and make it equal to str1
#otherwise, return false
def switchOne(str1, str2): #str1 is smaller, str2 is larger 
    count=0
    for x in range(len(str2)):
        if str1 == sliceString(str2, x):
            count+=1
    if count==1:
        return True
    else:
        return False

#returns string with the char at the specified index sliced out 
def sliceString(str, index):
    newstr=''
    for x in range(len(str)):
        if x!=index:
            newstr+=str[x]
    return newstr   



print(oneAway("hello", "heeloh")) #false
print(oneAway("bye", "byee")) #false
print(oneAway("bye", "byea")) #true
print(oneAway("bye", "beye")) #true