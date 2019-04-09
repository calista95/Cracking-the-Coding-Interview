#Program: Triple step
#Description: A child is running up a staircase with n steps and can hop either 1 step,
#2 steps, or 3 steps at a time. Implement a method to count how many possible ways to
#run up the stairs.
#Notes: use memoization 
#Runtime: O(n)

def count(n, memo): #take in number of total steps and an array list to memo everything 
    if n<0: #base case: number of steps is a negative number 
        return 0
    elif (n==0): #base case: number of steps is exactly 0 so there is only one way
        return 1
    elif (memo[n] > -1): #something already stored in the array position, return the value stored at that location 
        return memo[n] 
    else: #this means that memo[n] == -1, so nothing has been memoized at this location just yet 
        memo[n]=count(n-1, memo)+count(n-2, memo)+count(n-3, memo)
        return memo[n]

def countWays(n):
    memo = [-1]*(n+1)
    print(count(n, memo))
    print(memo)


countWays(5)