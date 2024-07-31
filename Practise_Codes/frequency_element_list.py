

def frequency_element(value):
    dict = {}
    for i in value:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i] = 1            
    return dict                  

n = int(input("Enter the no of elements in list: "))
ltr=[]
for i in range(n):
    ltr.append(input("Enter the items: "))
    
print(f"frequency of each elemnt in list{frequency_element(ltr)}")    
    
