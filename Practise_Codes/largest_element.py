
def largest_element(value):
    value.sort(reverse=True) #the sort function works in place, therefor if u assign it to a variable it will return none
    return value[0]

lst=[]
n=int(input("Enter the no of elements: "))

for i in range(0,n):
    ele = int(input())
    lst.append(ele)
    
print(lst)    
    
print(f"larget element in the list is {largest_element(lst)}") 


