def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """


    answer =[]
    for i in range(B,A):
        answer.append(i)
    return answer
print(main(10,5))