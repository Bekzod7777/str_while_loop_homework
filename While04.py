def main(s):
    i=0
    t=0
    while len(s)>t:
        if s[t]==s[t].upper():
            i +=1
        t +=1
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return  i

