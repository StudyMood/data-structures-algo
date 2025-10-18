# This is doubly_Iinklist.py
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None   # previous node ka address
        self.next = None   # next node ka address
#Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None   # pehla node
#Append Function (Add Node at End)
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:          # last node tak jao
            temp = temp.next
        temp.next = new_node      # last node ke next me new node jodo
        new_node.prev = temp      # new node ke prev me last node jodo
#Display Function (Forward & Backward)
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            last = temp
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head
        if temp is None:
            return
        # last node tak jao
        while temp.next:
            temp = temp.next
        # ab reverse print karo
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("None")

# 🧪 Test
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

print("Forward Traversal:")
dll.display_forward()

print("Backward Traversal:")
dll.display_backward()
