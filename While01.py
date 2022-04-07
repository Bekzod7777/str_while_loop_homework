def main(s):
    i=0
    t=0
    while len(s)>t:
        if s[t].isdigit()==True:
            i +=1
        t +=1
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return  i
