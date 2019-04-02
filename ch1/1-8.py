#Program 8 Chapter 1 
#Name: zero matrix
# #Runtime: O(nm)
#Date: 4/2/2019
#Notes: 

#get a list of the array positions with zero
def zero(array, zerospots):
    iter=0
    for x in range(len(array)):
        for y in range(len(array)):
            if array[x][y] ==0:
                zerospots[iter].append(x)
                zerospots[iter].append(y)
                iter+=1

#apply zeros to the array's rows and columns 
def apply(array, zerospots):
    for x in zerospots: #for each entry in the zerospots list 
        #set columns and rows 
        for y in range(len(array)):
            array[x[0]][y] = 0 #x[0] is the row
            array[y][x[1]] = 0 #x[1] is the column 
            
array = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]

zerospots = [[]] 

zero(array, zerospots)
apply(array, zerospots)

#print out new array 
for x in array:
    print(x)