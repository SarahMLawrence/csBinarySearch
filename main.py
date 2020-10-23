def csBinarySearch(nums, target):
    min_idx = 0
    max_idx = len(nums) -1
    if_found = False
    while min_idx <= max_idx and not if_found:
        mid_idx = (min_idx + max_idx) // 2
        
        if nums[mid_idx] == target:
            if_found = True
        
        elif target < nums[mid_idx]:
            max_idx = mid_idx - 1
            
        else: 
            min_idx = mid_idx + 1
            
    if if_found == True:
        return (mid_idx)


        
    return -1   

