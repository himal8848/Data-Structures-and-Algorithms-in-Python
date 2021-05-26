#Linear Search In Python
#Time complexity is O(n)

def linear_search(list,target):
    
    for i in range(len(list)):
        if list[i] == target:
            print("Found at Index ",i)
            break
    else:
        print("Not Found")
    
list = [4,6,8,1,3,5]
target = 5

linear_search(list,target)