#Program 3 Chapter 1 
#Name: Replace spaces
#Runtime: O(n)
#Date: 3/28/2019

def replaceSpaces(str):
    result=''
    for x in str:
        if x == ' ':
            result += '%20'
        else:
            result+=x
    return result

print(replaceSpaces("Mr John Smith")) #expected Mr%20John%20Smith
print(replaceSpaces("hi  bye  hi  bye")) #expected hi%20%20bye%20%20hi%20%20bye