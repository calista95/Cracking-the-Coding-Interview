#Program 9 Chapter 1 
#Name: string rotation
# #Runtime: O(n)
#Date: 4/2/2019
#Notes: Given s1 (the unrotated string) and s2 (the rotated string), s2 will always be a substring of s1s1.


def rotation(str1, str2):
    if len(str1) == len(str2):
        str1str1 = str1 + str1
        if str2 in str1str1:
            return True
        return False
    else:
        return False


print(rotation("waterbottle", "erbottlewat")) #true
print(rotation("waterbottle", "elbottlewat")) #false