
# Node Class
class Node: 
    def __init__(self, value):
        self.value = value
        self.pre_node = None
        self.next = None

#Doubly LinkedList
class DoublyLinkedList:
    # MARK: Basic Functions
    def __init__(self, value):
        new_node = Node(value)
        self.tail = new_node
        self.head = new_node
        self.length = 1
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
    # MARK: Append
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.pre_node = self.tail
            self.tail = new_node
            self.length += 1
        return True
    # MARK: pop
    def pop(self):
        if self.tail is None:
            return None
        tmp_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        self.tail = self.tail.pre_node
        self.tail.next = None
        tmp_node.pre_node = None
        self.length -= 1
        return tmp_node

    # MARK: prepend
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.pre_node = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True



       


# Demo 
my_doubly_link_list = DoublyLinkedList(7)
my_doubly_link_list.print_list()

print('append')
my_doubly_link_list.append(8)
my_doubly_link_list.print_list()
print(my_doubly_link_list.tail.value)
print(my_doubly_link_list.tail.pre_node.value)
print('-----')

print('pop')
my_doubly_link_list.pop()
my_doubly_link_list.print_list()
print('-----')

print('prepend')
my_doubly_link_list.prepend(6)
my_doubly_link_list.print_list()
print('-----')