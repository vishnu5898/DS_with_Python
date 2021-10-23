def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_ind = i
        for j in range(i+1,n):
            if(arr[j] < arr[min_ind]):
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]

array = [5,4,10,12,3,6]
selection_sort(array)
print(array)