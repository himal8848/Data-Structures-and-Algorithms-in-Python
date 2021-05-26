#Selection Sort in Python


def selection_sort(list):

    for i in range(len(list)):
        minpos = i 
        for j in range(i+1,len(list)):
            if list[j] < list[minpos]:
                minpos = j

        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp

    print(list)

list = [23,12,8,9,25,13,6]
selection_sort(list)
