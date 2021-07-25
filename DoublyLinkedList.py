class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def last_node(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        return temp

    # def print_forward(self):
    #     if self.head is None:
    #         print('Linked List is empty..')
    #         return
    #     temp = self.head
    #     ll = ''
    #     while temp:
    #         ll += temp.data + '->'
    #         temp = temp.next

    #     print(ll + 'None')

    def insert(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data,None,temp)

    # def print_backward(self):
    #     if self.head is None:
    #         print('Linked List is empty..')
    #         return
    #     last_node = self.last_node()
    #     temp = last_node
    #     ll = ''
    #     while temp:
    #         ll += '->' + temp.data
    #         temp = temp.prev

    #     print('None' + ll)

    def show(self, direction = 'forward'):
        if self.head is None:
            print('Linked List is empty.')
            return

        if direction == 'forward':
            temp = self.head
            ll = ''
            while temp:
                ll += temp.data + '->'
                temp = temp.next
            print(ll + 'None')  
        if direction == 'backward':
            last_node = self.last_node()
            temp = last_node
            ll = ''
            while temp:
                ll += '->' + temp.data
                temp = temp.prev
            print('None' + ll)  
        else:
            raise Exception('Invalid Argument!')

if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert('shrawan')
    ll.insert('muzakkir')
    ll.insert('tavez')
    ll.insert('narayan')

    ll.show('up')
    


    