class Node:
    def __init__(self, data):
        self.data= data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    
    def push(self, data):
        new_node =  Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print('need to previous node')
            return
        new_node = Node(data)
        new_node.next = prev_node.next 
        prev_node.next = new_node

    def delete_node(self, key):
        temp = self.head

        if temp is not None and temp.data == key:
            self.head = temp.next
            return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
            
        if temp is None:
            print("no data")
            return
        
        prev.next = temp.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end='→')
            temp = temp.next
        print("None")



llist = LinkedList()
llist.append(10)
llist.append(20)
llist.push(5)
llist.append(30)
llist.insert_after(llist.head.next, 15)

print("Linked List")
llist.print_list()