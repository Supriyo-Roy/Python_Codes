arr1 = [3,1,9,7,1,2,4]  
# we can also use max=max(arr1)
def max_element(arr1):    
    d=0
    for i in range (len(arr1)):
        if arr1[i] > d:
            d = arr1[i]
    return d        
     
max = max_element(arr1)

#craete an new array/list that will have the size of max(arr1) +1 and initilizw it with zero
count=[0]*(max+1)

#iterate through the main array(arr1) for each value, increment the value by 1 of new array in index of arr1 value 

for i in arr1:
    count[i]+=1
    
 #create a new array/list 
sorted=[]
for i in range (len(count)):
    while count[i]!=0:
        count[i]-=1
        sorted.append(i)
        


print(sorted)


#link to understand concept --> https://www.youtube.com/watch?v=HkvChUv9dDg



        
            
     
 

