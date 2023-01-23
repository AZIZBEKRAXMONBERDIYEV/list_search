def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    mx=data[0]
    i=0
    while i<len(data):
        if mx<data[i]:
            s=data[i]
        i+=1
    return data.count(mx)
print(find_max_count([12, 2, 5, 2, 7, 9, 1]))
    
