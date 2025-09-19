# Bubble sort

array = [12, 4, 56, 87, 6, 3]


def BubbleSort(array):
    for i in range(0,len(array)):
        for j in range(i + 1, len(array)):
            if array[j]>  array[i]:
                array[j], array[i] = array[i], array[j]
    print(array)


BubbleSort(array)
