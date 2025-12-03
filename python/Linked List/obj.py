class Node:
    def __init__(self, data):
        self.data = data      
        self.next = None      

class LinkedList:
    def __init__(self):
        self.head = None      

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        current_node = self.head

     
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

     
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            print(f"Node with data {key} not found.")
            return

        prev.next = current_node.next
        current_node = None


    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("end")
    def delete_first(self):
        
        if self.head is None:
            print("empty")
            return

       
        self.head = self.head.next
    def delete_last(self):
        
        if self.head is None:
            print("List is empty")
            return

        
        if self.head.next is None:
            self.head = None
            return

        
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next

        
        second_last.next = None
        def delete_at_index(self, index):

            if self.head is None:
                print("List is empty")
                return

            if index == 0:
                self.head = self.head.next
                return

            current = self.head
            position = 0


            while current is not None and position < index - 1:
                current = current.next
                position += 1

          
            if current is None or current.next is None:
                print("Index out of bounds")
                return


            current.next = current.next.next
