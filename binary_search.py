#Binary search using iterative process 
#List must be sorted in asc order 
#Time complexity is O(log n) and constant space

def binary_search(list,target):
    
    first = 0
    last = len(list) - 1

    while first <= last:
        
        mid = (first+last)//2

        if list[mid] == target:
            return True

        elif(list[mid] < target):
            first = mid + 1

        elif(list[mid] > target):
            last = mid - 1

        else:
            return False

list = [3,6,8,9,12,33]
target = 13

print(binary_search(list,target))


#Using Recursive Function

def binary_recusrsive_search(list,target):

    if len(list) == 0:
        return False
    else:
        mid = (len(list))//2

        if list[mid] ==  target:
            return True
        
        elif list[mid] < target:
            return binary_recusrsive_search(list[mid+1:],target)
        
        else:
            return binary_recusrsive_search(list[:mid],target)



list = [3,6,8,9,12,33]
target = 12

print(binary_recusrsive_search(list,target))


