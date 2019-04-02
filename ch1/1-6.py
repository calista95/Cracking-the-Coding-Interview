#Program 5 Chapter 1 
#Name: String Compression
#Runtime: O(n)
#Date: 4/1/2019
#Notes: 

def compress(str):
    cur='' #current
    prev='' #previous
    newstr=''
    for x in str:
        cur=x #set current
        if x != prev:
            newstr+=x
        prev=x
    return newstr

print(compress("sssttrrringgg")) #string
print(compress("hiiiiiiiiiiiiiiiiiiiiiiiiiii")) #hi