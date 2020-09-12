# Much like the other function to find the index of value in a sorted list, this one list the closest overall index for a number

def seek_closest_index(n,target_list):
    
    tl = target_list

    value_list = seek_value_index(n,target_list)
    
    bi = value_list[0]
    ei = value_list[1]
        
    closen_one = None
    
    if abs((tl[bi]-n)**2)<=abs((tl[ei]-n)**2):
        closen_one = bi
    else:
        closen_one = ei
        
    return closen_one
