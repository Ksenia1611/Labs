
class Node:
    def __init__(self , date = None):
        self.data = date
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    # Добавление элемента в начало списка
    def insert_at_start(self, new_data):
        new_node = Node(new_data)
        if self.first is not None:
            self.first.prev = new_node
            new_node.next = self.first
            self.first = new_node
        else:
            self.first = self.last = new_node    
    
    # Добавление элемента в конец списка
    def insert_at_end(self, new_data):
        new_data = Node(new_data)
        if self.first is not None:
            self.last.next = new_data
            new_data.prev = self.last
            self.last = new_data
        else:
             self.first = self.last = new_data

     # Удаление первого элемента
    def remove_first_element(self):
        if self.first is not None:
            self.first = self.first.next
            self.first.prev = None
        else:
            print("Cписок пуст")

     # Удаление последнего элемента   
    def remove_last_element(self):
        if self.first is not None:
            self.current = self.first
            self.last = self.last.prev
            self.last.next = None
            if self.current.next is None:
                self.first = None
                self.last = None
            else:
                print("Список пуст")
    
    # Нахождение узла
    def node(self, node):
        current = self.first
        while current is not None:
            if current.data == node:
                print('True')
                return True
            else:
                current = current.next
        print('False')
        return False
                
    # Печать списка
    def print_list(self):
        value_to_print = self.first
        if self.first is None:
            print("Список пуст") 
            return
        print("Узлы двусвязного списка: "); 
        while value_to_print is not None:
            print(value_to_print.data)
            value_to_print = value_to_print.next

class Interface:

    def __init__(self):
        self.linked_list = DoubleLinkedList()

    def print_linked_list(self):
        self.linked_list.print_list()

    def node(self, node):
        self.linked_list.node(node)
    
    def add_end(self, value):
        self.linked_list.insert_at_end(value)

    def add_first(self, value):
        self.linked_list.insert_at_start(value)

    def pop_first(self):
        self.linked_list.remove_first_element()

    def pop_last(self):
        self.linked_list.remove_last_element()


dll = Interface()
dll.add_end(5)
dll.add_end(3)
dll.add_end(6)
dll.add_first(55)
dll.add_first(9)
dll.node(4)
dll.pop_first()
dll.print_linked_list()