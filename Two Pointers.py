# same direction - fixed size / dynamic size
# Opposite direction - fixed size / dynamic size

## (same direction) If fast pointer overlaps slow pointer -> cycle

# Palindromes
# Reversals
# Merging sorted data
# "K" sized comparisons

def is_palindrome(s: str) -> bool:

    s_p , e_p = 0 , (len(s)-1)
    flag = True
    
    while s_p < e_p:
        
        if s[s_p].isalnum() and s[e_p].isalnum():
            if s[s_p].lower() == s[e_p].lower():
                s_p += 1
                e_p -= 1
                continue
            else:
                return False
            
        while not s[s_p].isalnum() and s_p < e_p:
            s_p += 1
        while not s[e_p].isalnum() and s_p < e_p:
            e_p -= 1

    return flag


def is_palindrome2(s: str) -> bool:

    s_p , e_p = 0 , (len(s)-1)

    while s_p < e_p:
                 
        while not s[s_p].isalnum() and s_p < e_p:
            s_p += 1
        while not s[e_p].isalnum() and s_p < e_p:
            e_p -= 1

        if s[s_p].lower() != s[e_p].lower():
            return False
        
        s_p += 1
        e_p -= 1
        
    return True

