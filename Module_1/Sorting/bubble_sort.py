def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if(arr[j+1] < arr[j]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if(swapped == False):
            return

array = [3,6,8,4,10,2]
bubble_sort(array)
print(array)