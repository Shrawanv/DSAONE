class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        count = 0
        temp = self.head 
        while temp.next is not None:
            temp  = temp.next
            count += 1
        return count + 1

    def delete(self, data):
        if self.head is None:
            print('Nothing to delete, Linkedlist is empty')
        temp = self.head
        while temp:
            if temp.next.data == data:
                temp.next = temp.next.next
                break
            temp = temp.next
    
    def delete_at(self, pos):
        if pos < 0 or pos >= self.length():
            raise Exception('Invalid Index')
        if self.head is None:
            print('Linked is empty, nothing to delete')
            return
        count = 0
        prev = self.head 
        while prev:
            if count == pos-1:
                prev.next = prev.next.next
                return
            prev = prev.next
            count += 1

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def insert_at(self,data,pos):
        if pos < 0 or pos > self.length():
            raise Exception('Invalid Index')
        if pos == 0:
            if self.head is None:
                self.insert(data)
                return
            temp = self.head
            self.head = Node(data)
            self.head.next = temp
            return
        prev = self.head
        count = 0
        while count != pos - 1 :
            prev = prev.next
            count += 1
        temp = prev.next
        prev.next = Node(data)
        prev.next.next = temp

    def insert_values(self,l):
        for i in l:
            self.insert(i)

    def show(self):
        if self.head is None:
            print('linked list is empty')
            return 
        temp = self.head 
        ll = ''
        while temp:
            ll += str(temp.data) + '-->'
            temp = temp.next
        ll += 'None'
        print(ll)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert('mango')
    ll.show()