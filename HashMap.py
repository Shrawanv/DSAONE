# In python HashMap is Dictionary Implementation.
class HashMap:
    def __init__(self,Max):
        self.Max = Max
        self.arr = [None for element in range(self.Max)]

    def hash(self, key):
        hash = 0
        for element in key:
            hash += ord(element)
        return hash%self.Max

    def __setitem__(self, key, value):
        h = self.hash(key)
        self.arr[h] = value
        
    def __getitem__(self, key):
        h = self.hash(key)
        print(self.arr[h])
        

if __name__ == '__main__':
    pricetable = HashMap(10)
    # pricetable.set_item('march 6',300)
    # pricetable.set_item('april 9', 350)

    # pricetable.get_item('april 9')
    # print(pricetable.hash('march 6'))
    pricetable['march 6'] = 300
    pricetable['april 9'] = 350
    pricetable['may 12'] = 310
    pricetable['june 16'] = 325
    pricetable['may 12']
    
