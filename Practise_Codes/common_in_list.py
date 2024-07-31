def common_elements_finder(l1,l2):
    common_list = set()
    for i in l1:
        if i in l2:
            common_list.add(i)
    return common_list    
          
    
 
lst=[]
lst2=[]

n = int(input("Enter tottal no of elements in List : "))
for i in range(n):
    lst.append(input("Enter the element in list 1: "))
    lst2.append(input("Enter element in list 2: "))
    
print(f"List 1 {lst}")
print(f"List 2 {lst2}")
print(f"Common elements in the lists{common_elements_finder(lst,lst2)}")    


        
