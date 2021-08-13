from sort012 import swap

# 3 pointer approach
def move_negetive(arr): 
    left = 0
    mid = 0
    right = len(arr)-1

    while left <= right:
        if arr[mid] < 0:
            swap(arr,left,mid)
            left += 1
            mid += 1
        else:
            swap(arr,right,mid)
            right -= 1
    return arr


# 2 pointer approach 
def move_negative2(arr):
    left = 0
    right = len(arr) -1 

    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] > 0 and arr[right] < 0:
            swap(arr,left,right)
            left += 1
            right -= 1
        elif arr[left] > 0 and arr[right] > 0:
            right -= 1
        else:
            left += 1
            right -= 1
    return arr

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    # print(move_negetive(arr))
    print(move_negative2(arr))