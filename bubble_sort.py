#Bubble Sort in Python

def bubble_sort(list):

    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

list = [23,12,8,9,25,13,6]
result = bubble_sort(list)
print(list)