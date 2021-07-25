no = int(input("Enter number: "))

def numSetBits(no):
    count = 0
    while no > 0:
        no &= (no -1)
        count += 1
    return count

print(numSetBits(no))