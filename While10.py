def main(s):
    s=int(s)
    t=0
    i=0
    while s>0:

        n=s%10
        s=s//10
        if n%2==1:
            t +=n
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return t


