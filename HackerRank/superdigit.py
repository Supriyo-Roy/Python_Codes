n = '1'
# v = n*5
# print(v)

def sum_finder(s, k):
    new_s=s*k
    print(new_s)
    sum = 0
    int_n = int(new_s)
    print(int_n)
    while int_n > 0:
        k = int_n % 10
        sum = int(sum + k)
        print(f"Sum={sum}")
        int_n = int(int_n/10)
        print(int_n)
        print(f"length of sum {len(str(sum))}")
    print("Out of loop")
    p = sum
    print(f"p is {p} and sum is {sum}")
    print(f"length of p is {len(str(p))}")
    if len(str(p)) > 1:
        return sum_finder(str(p), 1)
    else:
        return sum
          
print(f"superdigit is = {sum_finder(n, 4)}")    

