def merge(arr, low, mid, high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    i = 0
    j = 0
    k = low
    while(i < len(left) and j < len(right)):
        if(left[i] <= right[j]):
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1
    while(i < len(left)):
        arr[k] = left[i]
        k += 1
        i += 1
    while(j < len(right)):
        arr[k] = right[j]
        k += 1
        j += 1

def merge_sort(arr, low, high):
    if(low < high):
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)

array = [4,6,2,10,12,1,15,8]
merge_sort(array, 0, 7)
print(array)