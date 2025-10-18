#create node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#create linklist
class LinkedList:
    def __init__(self):
        self.head = None
#Node add karna (append)
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
#Display karna
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Linked List banana
ll = LinkedList()
ll.append(10)
ll.append(40)
ll.append(20)
ll.append(30)

# Display
ll.display()
# This is singly_linklist.py
