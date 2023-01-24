def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    mx=data[0]
    i=0
    while i<len(data):
        if  data[i]%2==0:
            s=data[i]
        
        """if mx<data[i]:
            mx=data[i]"""
            
        
            
        i+=1
    return s
print(find_max_even([13,4,10,3,7,1,9]))
    
