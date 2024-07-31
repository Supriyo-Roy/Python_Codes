def prime_finder(value):
    d = 0
    for i in range(1,value):
        if value % i == 0:
            d+=1
    if d == 1:
        return True
nums = int(input("Enter your number to check prime"))
if prime_finder(nums):
    print(f"{nums} is prime number")
else:
    print(f"{nums} is not prime")    