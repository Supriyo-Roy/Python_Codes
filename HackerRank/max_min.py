#Question
# https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# num = [1,2,3,4,5], [22,34,55,23,12]

# 1+2+3+4 = 10        12+22+23+34 = 91
# 2+3+4+5 = 14        22+23+34+55 = 134


#My Initial approach
def minMaxSum(arr):
    arr.sort()
    n = len(arr)
    minSum=0
    maxSum=0
    for i in range(0,n-1):
        minSum=minSum+arr[i]
    for i in range(1,n):
        maxSum=maxSum+arr[i]
    print(f"{maxSum} {minSum}")



list1 = [1,2,3,4,5]    
print(f"{minMaxSum(list1)}")    

# list2=list1[0:-1]
# list3=list1[1:]
# print(list2,list3)


    
           
        

