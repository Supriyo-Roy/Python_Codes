alpha="abcdefghijklmnopqrstuvwxyz"
s="Always-Look-on-the-Bright-Side-of-Life"
k =5
new_str=alpha[k:]+alpha[:k]
r=""

for char in s:
        if char.isupper():
            new_char=char.lower()
            new_index_char=(new_str.index(new_char)+k) % 26
            print(new_index_char)
            new_upper=new_str[new_index_char].upper()
            r=r+new_upper
        elif char.islower():    
            new_index_char=(new_str.index(char)+k) % 26
            r=r+new_str[new_index_char]
        else:
            r=r+char    
print(r)       

##Let's say you want to shift a letter by 30 positions in the alphabet.

# Without Wrapping: The index would be 30, which is greater than 25.

# With Wrapping: You use 30 % 26:

# Divide 30 by 26. The remainder of this division is 4 (because 30 - (26 * 1) = 4).
# So, 30 % 26 = 4. This means you wrap around to the 4th position in the alphabet, which is 'e'.