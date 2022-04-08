def main(s):
    t=0
    i=0
    while s>0:
        n=s%10
        s=s//10
        if n%2==0:
            i+=1

        
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """   
    return  i
