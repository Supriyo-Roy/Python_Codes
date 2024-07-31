def factorial(n):
    result = 1
    for i in range(1,n+1): #range takes 3 input (start,stop,step) stop in exclusive like (1,5) it will go 1,2,3,4
        result = result *i
    return result
number = int(input("Please insert your no to find factorial "))
print(f"The factorial of {number} is {factorial(number)}")    