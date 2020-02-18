def recursive_search(arr, x, l, r):
    
    if r < l:
        return -1
    if arr[l] == x or arr[r] == x: 
        return True
    else:
        return False
    return recursive_search(arr, l+1, r-1, x) 

