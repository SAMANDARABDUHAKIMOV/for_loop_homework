def main(k,n):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    answer=[]
    for i in range(n):
        answer.append(k)
    return answer 

print(main(3,5))