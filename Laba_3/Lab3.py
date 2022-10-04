from ast import Delete


class Node:
    def __init__(self , date = None):
        self.data = date
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

     # Получение узла по индексу
    def get_data(self, data_index):
        try:
            last = self.head_value
            node_index = 0
            while node_index <= data_index:
                if node_index == data_index:
                    return last.data_value
                node_index += 1
                last = last.next_value
        except Exception:
            print('Индекса не существет')


    # Добавление элемента в начало списка
    def insert_at_start(self, new_data):
        new_node = Node(new_data)
        if self.first is not None:
            new_node.next = self.first
            self.first = new_node
        else:
            self.first = new_node    
    
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
            delIt = self.first
            self.first = self.first.next
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
                print("Error: List is empty")
                
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

class LLInterface:
    def __init__(self):
        self.linked_list = DoubleLinkedList()

    def print_linked_list(self):
        self.linked_list.print_list()
    
    
    def add_end(self, value):
        self.linked_list.insert_at_end(value)

    def add_first(self, value):
        self.linked_list.insert_at_start(value)

    def pop_first(self):
        self.linked_list.remove_first_element()

    def pop_last(self):
        self.linked_list.remove_last_element()


ll = LLInterface()
ll.add_end(5)
ll.add_end(3)
ll.add_end(6)
ll.add_first(55)
ll.add_first(9)
ll.pop_last()
ll.print_linked_list()