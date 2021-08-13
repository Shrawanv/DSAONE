def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)

    merge(left,right,arr)

def merge(left_arr,right_arr,arr):
    len_a = len(left_arr)
    len_b = len(right_arr)
    i = j = k = 0

    while i < len_a and j < len_b:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len_a:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = right_arr[j]
        j += 1
        k += 1

if __name__ == '__main__':
    arr = [5,5,1,4,2,6,3,5,8,0,10]
    merge_sort(arr)
    print(arr)
