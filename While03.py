def main(s):
   
    i=0
    t=0
    while len(s)>t:
        if not (s[t].isdigit() or s[t].isalpha()):

            i +=1
        t +=1
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return i

