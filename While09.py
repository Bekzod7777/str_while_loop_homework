def main(s):
    s=int(s)
    t=0
    i=0
    while s>0:

        n=s%10
        s=s//10
        t +=n
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return  t
