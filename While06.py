def main(s):
    unli=['A','O','E','I','U','a','o','e','i','u']
    t=0
    i=0
    while len(s)>t:
        if(s[t] not in unli)  and s[t].isalpha():
            i +=1
        t +=1
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    return i
