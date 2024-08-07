s="cbc"


def palindromIndex(s):
    d=0
    new_str=""
    rrev=s[::-1]
    if s == rrev:
        return "palindrom"
    else:
            while d < len(s):
                new_str = s[:d] + s[d+1:]
                reversed=new_str[::-1]
                if new_str == reversed:
                    return d
                d=d+1    
print(f"{palindromIndex(s)}")
      
            
            
