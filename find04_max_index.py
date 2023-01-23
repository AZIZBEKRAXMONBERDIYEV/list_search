def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    mx=data[0]
    i=0
    while i<len(data):
        if mx<data[i]:
            mx=data[i]
        

            
        i+=1
    return data.index(mx)
print(find_max_index([12,4,5,3,7,2,9]))
    
