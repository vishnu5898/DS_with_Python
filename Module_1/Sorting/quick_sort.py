def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while(True):
        i += 1
        while(arr[i] < pivot):
            i += 1
        j -= 1
        while(arr[j] > pivot):
            j -= 1
        if(i >= j):
            return j
        arr[i], arr[j] = arr[j], arr[i]

def hoare_quick_sort(arr,low,high):
    while(low < high):
        p = hoare_partition(arr, low, high)
        hoare_quick_sort(arr, low, p)
        low = p + 1

def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if(arr[j] < pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def lomuto_quick_sort(arr, low, high):
    while(low < high):
        p = lomuto_partition(arr, low, high)
        lomuto_quick_sort(arr, low, p-1)
        low = p + 1

array1 = [3,4,42,12,10,7]
array2 = [3,4,42,12,10,7]
a = hoare_quick_sort(array1, 0, 5)
b = lomuto_quick_sort(array2, 0, 5)
print(array1)
print(array1)