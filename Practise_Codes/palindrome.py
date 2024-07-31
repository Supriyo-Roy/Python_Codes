def is_palindrome(value):
    reversed_string = value[::-1] #slicing [start:stop:stepcount]
    return reversed_string == value #returns true or false

value = input("Enter your string: ")
if is_palindrome(value):
    print("Your string is a palindrome")
else:
    print("Your string is not a palindrome")    
    
    
    
    
    
    