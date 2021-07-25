arr  = list(map(int, input('enter list values: ').split()))
k = int(input('enter k value: '))

def unique_element(arr, k):
    arr = sorted(arr)
    index = 1
    if arr[0] != arr[1]:
        return arr[0]
    elif arr[-1] != arr[-2]:
        return arr[-1]
    else:
        while index < len(arr):
            if arr[index] != arr[index - 1]:
                return arr[index - 1]
            else:
                index += k

print(unique_element(arr, k))