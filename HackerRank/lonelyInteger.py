
def lonelyInteger(arr):
    n= len(l1)
    d=0
    for i in range(0,n):
        d=0
        for j in range(0,n):
            if l1[i] == l1[j]:
                d=d+1
        if d == 1:
            break
    return l1[i]   

l1 = [12,55,13,14,12,55,66]             

print(f"{lonelyInteger(l1)}")    