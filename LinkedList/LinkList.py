class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.count = 1

    # print_list 印出 LinkedList 中的所有 value
    def print_list(self):
        tempNode = self.head
        while tempNode is not None:
            print(tempNode.value)
            tempNode = tempNode.next
    # append 將一個新元素加入到 LinkedList 中
    def append(self, value):
        new_node = Node(value)
        # 須考慮完全沒有任何元素的情況
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
        return True
    #pop 將最後一個元素回傳
    def pop(self):
        preNode = self.head
        tempNode = self.head
        if self.tail is None:
            return None
        if self.tail == self.head:
            tailNode = self.tail
            self.tail = None
            self.head = None
            self.count = 0
            return tailNode
        else:
            while(tempNode.next):
                preNode = tempNode
                tempNode = tempNode.next
            self.tail = preNode
            self.tail.next = None
            self.count -= 1
            if self.count == 0:
                self.head = None
                self.tail = None
        return tempNode

    #prepend 將一個元素加入在第一個位置 (head)
    def prepend(self, value):
        new_node = Node(value)
        # 如果現在長度是空的，則初始化
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count += 1
        return True

    def popFirst(self):
        #將第一個元素 pop，須考慮只有一個元素或者沒有任何元素的情況
        if self.count == 0:
            return None
        else:
            tmpNode = self.head
            self.head = self.head.next
            tmpNode.next = None
            self.count -= 1
            if self.count == 0: 
                self.tail = None
            return tmpNode

    def get(self, index):
        # 根據傳入的 index，回傳對應的 Node
        # 須考慮 index 範圍的問題
        if index < 0 or index >= self.count:
            return None
        countNum = 0
        currentNode = self.head
        while(countNum != index):
            currentNode = currentNode.next
            countNum += 1
        return currentNode

    # 取出對應的 Node 之後取代原本的 value
    def set_value(self, value, index):
        tmp_node = self.get(index)
        if (tmp_node):
            tmp_node.value = value
            return True
        return False

    # 在相對應的 index 插入一個值
    def insert_value(self, value, index):
        if index < 0 or index > self.count:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.count:
            return self.append(value) 
        pre_node = self.get(index - 1)
        new_node = Node(value)
        new_node.next = pre_node.next
        pre_node.next = new_node
        self.count += 1
        return True
    # 在相對應的 index 中，移除 Node
    def remove(self, index):
        if index < 0 or index >= self.count:
            return False
        if index == 0:
            return self.popFirst()
        if index == self.count - 1:
            return self.pop()
        pre_current_node = self.get(index - 1)
        tmp_node = pre_current_node.next
        pre_current_node.next = tmp_node.next
        tmp_node.next = None
        self.count -= 1
        return tmp_node

    # 回傳相反的 LinkedList
    def reverse(self):
        # 把每一個元素抓出來後，將每一個的 Node 的 next 指回自己的 pre node，直到最後結束
        current_node = self.head
        pre_node = None
        while current_node is not None:
            original_next_node = current_node.next
            current_node.next = pre_node
            pre_node = current_node
            current_node = original_next_node
        # switch head & tail
        tmp_head_node = self.head
        self.head = self.tail
        self.tail = tmp_head_node


        


print('reverse')
linked_list = LinkList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.reverse()
linked_list.reverse()
linked_list.reverse()
linked_list.print_list()
print('-----')    


print('create')
my_linked_list = LinkList(4)
my_linked_list.print_list()
print('-----')
#print(my_linked_list.head.value)
#print(my_linked_list.tail.value)
print('append')
my_linked_list.append(5)
print('-----')
print('prepend')
my_linked_list.prepend(7)
my_linked_list.print_list()
print('-----')
print('get')
print(my_linked_list.get(1).value)
print('-----')
print('insert_value')
my_linked_list.insert_value(77,2)
my_linked_list.print_list()
print('-----')
print('remove')
my_linked_list.remove(2)
my_linked_list.print_list()
print('-----')
print('set_value')
my_linked_list.set_value(88, 2)
my_linked_list.print_list()
print('-----')
print('pop first')
print(my_linked_list.popFirst().value)
my_linked_list.print_list()
print('-----')
print('pop')
print(my_linked_list.pop().value)
print(my_linked_list.pop().value)
print(my_linked_list.pop().value)
print('-----')

