#Sorted merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
#Write a method to merge B into A in sorted order
#Runtime: O(logn)
#Notes: Since you know that you have extra space at the end, you need to start from greatest to least instead of the 
#normal method. Start from the top index. 


def sort():
 
    a=[2,4,6, None, None, None]
    b=[1,3,5]


    indexMerged=5 #this is the index of the entirety of array A

    indexA=2 #last index of array A
    indexB=2 #last index of array B

    #No choice but to hardcode because I'm not sure how to get the number of filled elements in an array without 
    #a separate function!

    while indexB >=0:
        if indexA >=0 and a[indexA] > b[indexB]:
            a[indexMerged] = a[indexA]
            indexA-=1
        else:
            a[indexMerged] = b[indexB]
            indexB-=1
        indexMerged-=1
    print(a)



def main():
    sort()

if __name__ == "__main__":
    main()