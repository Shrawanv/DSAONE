
def swap(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]

def sort012(arr,n):
    '''This is very simple solution but the space complexity of this is O(n) 
    as it is creating 3 different array of total size of original n size array.'''
    sorted_arr = []
    ones = []
    twos = []
    for elem in arr:
        if elem == 0:
            sorted_arr.append(elem)
        elif elem == 1:
            ones.append(elem)
        else:
            twos.append(elem)
    sorted_arr.extend(ones)
    sorted_arr.extend(twos)

    return sorted_arr

def Sort012(arr,n):
    l = 0
    m = 0
    h = n-1
    while m <= h:
        if arr[m] == 0:
            swap(arr,l,m)
            l+=1
            m+=1
        elif arr[m] == 1:
            m+=1
        elif arr[m] == 2:
            swap(arr,h,m)
            h-=1
    return arr


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(Sort012(arr,n))
