
def heap_insert(arr,value):
    arr.append(value)
    i = len(arr) -1

    while i > 1:
        parent = i // 2
        if arr[parent] < arr[i]:
            arr[parent], arr[i] = arr[i], arr[parent]
            i = parent
        else:
            return

arr = [0,50,40,45,30,20,35,10]

heap_insert(arr,60)
heap_insert(arr,20)
print(arr)