def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    min=data[0]
    mx=data[0]
    i=0
    while i<len(data):
        if mx<data[i]:
            mx=data[i]
        if min>data[i]:
            min=data[i]
        i+=1
    return mx+min
print(find_max_min_sum([12, 2, 5, 2, 7, 12, 1]))
    
