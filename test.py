
# Třída pro buňku seznamu
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.data)
 
# Třída pro celý obousměrný spojový seznam
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    # vložení prvku na začátek, nic nevrací
    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node    
            new_node.prev = None    

    # Tisk seznamu pro kontrolu
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> " if current_node.next else "\n")
            current_node = current_node.next

    def contains(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    def clear(self):
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = None
            current_node.prev = None
            current_node.next = next_node


# Vytvoření seznamu a přidání uzlů
dll = DoublyLinkedList()
dll.insert_at_begin(5) # Přidání uzlu s hodnotou 3 na začátek
dll.insert_at_begin(2) # Přidání uzlu s hodnotou 2 na začátek
dll.insert_at_begin(4) # Přidání uzlu s hodnotou 1 na začátek
dll.clear()
# Procházení seznamu a tisk hodnot
dll.print_list()