#Program 1 Chapter 3 
#Name: Three in one 
#Runtime: O(1)
#Date: 4/3/2019

#iterators for each "separate" array
first = 0
second = 5
third = 10

def addToArr(array, arrayNum, val):

    #global so that we can increment iterators 
    global first
    global second
    global third

    # 1/3 of full array
    if arrayNum == 1:
        if first <= 4:
            array[first] = val
            first+=1
        else:
            print("not enough space!")

    # 2/3 of full array
    elif arrayNum == 2:
        if second <= 9:
            array[second] = val
            second+=1
        else:
            print("not enough space!")

    # 3/3 of full array
    elif arrayNum ==3:
        if third <= 14:
            array[third] = val
            print(str(third))
            third+=1
        else:
            print("not enough space!")


def main():

    array = [None]*15
    
    #adding to first "array"
    addToArr(array, 1,100)
    print(array)
    addToArr(array, 1,100)
    print(array)
    addToArr(array, 1,100)
    print(array)
    addToArr(array, 1,100)
    print(array)
    addToArr(array, 1,100)
    print(array)
    addToArr(array, 1,100)
    print(array)

    addToArr(array, 2,200)
    print(array)
    addToArr(array, 2,200)
    print(array)
    addToArr(array, 2,200)
    print(array)
    addToArr(array, 2,200)
    print(array)
    addToArr(array, 2,200)
    print(array)
    addToArr(array, 2,200)
    print(array)

    addToArr(array, 3,300)
    print(array)
    addToArr(array, 3,300)
    print(array)
    addToArr(array, 3,300)
    print(array)
    addToArr(array, 3,300)
    print(array)
    addToArr(array, 3,300)
    print(array)
    addToArr(array, 3,300)
    print(array)

if __name__ == "__main__":
    main()








