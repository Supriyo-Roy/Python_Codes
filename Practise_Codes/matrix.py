#Here we are assuming the no fo rows = no of columns

def matrix(n):
    o = []
    for i in range(n):
        row=[]
        for j in range(n):
            row_val=int(input(f"Enter the value of 0[{i}][{j}]"))
            row.append(row_val)
        o.append(row) 
    return o
def diagonalDifference(n,arr):
    left_sum=0
    right_sum=0
    d=n-1
    absolute_diff=0
    for i in range(n):
         left_sum+=arr[i][i]
         right_sum+=arr[i][d]
         d-=1
    absolute_diff=abs(left_sum-right_sum)
    return absolute_diff     

r_c = int(input("Enter the no of rows and columns \n"))
print(diagonalDifference(r_c,matrix(r_c)))
       