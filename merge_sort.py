#Merge_sort in Python

def merge_sort(list):
    """
    sorts a list in ascending order 
    Returns a new sorted list 

    Divide: Find the midpoint of the list and divide into  into sublists
    Conquer:Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """

    if len(list) <= 1: # Stopping condition
        return list

    left_half,right_half = split(list) # In left half-54,26 and right_half = 62, 93, 44, 55
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left,right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right 
    """

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left,right

def merge(left,right):
    """
    Merges two lists (arrays),sorting them in the process
    Returns a new merged list
    """
    l = []
    i = 0 #Index for left list
    j = 0 #Index for right list

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i = i + 1
        else:
            l.append(right[j])
            j = j + 1
    
    while i < len(left):
        l.append(left[i])
        i = i + 1
    
    while j < len(right):
        l.append(right[j])
        j = j + 1
    
    return l

list = [54, 26, 33,62, 93, 44, 55]
l = merge_sort(list)
print(l)