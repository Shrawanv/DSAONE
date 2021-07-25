class HashMap:
    def __init__(self,Max):
        self.Max = Max
        self.arr = [[] for element in range(self.Max)]

    def hash(self, key):
        hash = 0
        for element in key:
            hash += ord(element)
        return hash%self.Max

    def __setitem__(self, key:str, value):
        h = self.hash(key)
        found = False
        for idx, element in enumerate(self.arr):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] == (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))
        
    def __getitem__(self, key):
        h = self.hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                print(f'Date:{element[0]} and price:{element[1]}')
    
    def __delitem__(self, key:str) -> None: 
        h = self.hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

            
if __name__ == '__main__':
    pricetable = HashMap(10)

    pricetable['march 6'] = 210
    pricetable['march 8'] = 290
    pricetable['march 17'] = 310
    pricetable['march 17']
    
    
