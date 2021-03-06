# This function finds the two closest indices for a value in a sorted list. If such value exists in the list, the two
# numbers are the same, otherwise, it lists where the indices of the closest floor number and closest ceiling number.

def seek_value_index(n,target_list):
    
    tl = target_list

    bi = 0
    ei = len(tl) - 1
    bv = tl[bi]
    ev = tl[ei]
    
    if n<bv or n>ev:
        return [None,None]

    values = [bi,ei]
    repeat_control = []

    while (True):

        if repeat_control == values:
            break
        else: 
            repeat_control = values.copy()

        ci = int((bi+ei)/2)
        cv = tl[ci]

        if cv>bv and cv<=n:
            bi = ci
            bv = tl[ci]
        if cv<ev and cv>=n:
            ei = ci
            ev = tl[ci]

        values = [bi,ei]
        
    return values
