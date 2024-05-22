# Testovací skript pro odevzdání zápočtového úkolu.
# Vytvoření obousměrného spojového seznamu se zarážkou.
# Doplňte všechny metody tak, aby to prošlo testy v dolní části souboru.
# Testy jsou rozděleny na osm levelů, které můžete plnit postupně

LEVEL = 1   # zde postupně měňte číslo od 1 až do 8, čímž si zpřístupníte testy k jednotlivým levelům

# Třída pro buňku seznamu
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    def __str__(self) -> str:
        return str(self.data)
 
# Třída pro celý obousměrný spojový seznam
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    # vložení prvku na začátek, nic nevrací
    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
     
    # smazání prvku na začátku, vrátí se hodnota v tomto prvku
    def delete_at_begin(self):
        if self.head == None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data
 
    # převod seznamu na string v dopředném pořadí ve formátu [data1, data2, data3, ...]
    def string_list(self):
        result = []
        for i in self:
            result.append(str(i))
        return result    
    # vrací řetězec str
    def __str__(self):
        result = " "
        for i in self:
            result += str(i) + "->"
        return result + "None"            
    
    # převod seznamu na string ve zpětném pořadí ve formátu [data3, data2, data1]
    # vrací řetězec str
    def str_reverse(self):
        result = " "
        for i in self:
            print(i)


    # vloží prvek na konec seznamu, nic nevrací
    def insert_at_end(self, data):
        pass

    # smaže prvek na konci seznamu, vrací jeho hodnotu
    def delete_at_end(self):
        pass

    # smaže první nalezená data podle hodnoty, nic nevrací
    def delete_data(self, data):
        
        

    # vrací True/False podle toho, zda je seznam prázdný nebo ne
    def empty(self):
        if self == None:
            return True
        else:
            return False
    
    # smaže celý seznam, nic nevrací
    def clear(self):
        return self.clear 

    # vrací True/False podle toho, zda se data nacházejí v seznamu
    def contains(self, data):
        if data in self:
            return True
        else:
            return False

    # seřadí data v seznamu, parametr asc určuje, zda vzestupně (True) nebo sestupně (False)
    def sort(self, asc = True, x = min(self), y= max(self)):
        pivot


# Zde začínají testy

if LEVEL >= 1:
# Testy, level 1
# převod na string a vkládání na začátek

    dll = DoublyLinkedList()
    assert str(dll) == '[]'

    dll.insert_at_begin(10)
    assert str(dll) == '[10]'

    dll.insert_at_begin(12)
    dll.insert_at_begin(13)
    assert str(dll) == '[13, 12, 10]'

    print("Level 1: OK")

if LEVEL >= 2:
# Testy, level 2
# mazání na začátku

    assert dll.delete_at_begin()==13
    assert str(dll) == '[12, 10]'

    assert dll.delete_at_begin()==12
    assert str(dll) == '[10]'

    assert dll.delete_at_begin()==10
    assert str(dll) == '[]'

    assert dll.delete_at_begin()==None
    assert str(dll) == '[]'

    print("Level 2: OK")

if LEVEL >= 3:
# Testy, level 3
# vkládání na konec a výpis pozadu

    cars = DoublyLinkedList()
    assert cars.str_reverse() == '[]'
    cars.insert_at_end("trabant")
    assert str(cars) == '[trabant]'
    assert cars.str_reverse() == '[trabant]'
    cars.insert_at_end("mazda")
    assert str(cars) == '[trabant, mazda]'
    assert cars.str_reverse() == '[mazda, trabant]'
    cars.insert_at_end("tesla")
    assert str(cars) == '[trabant, mazda, tesla]'
    assert cars.str_reverse() == '[tesla, mazda, trabant]'
    cars.insert_at_begin("skoda")
    assert str(cars) == '[skoda, trabant, mazda, tesla]'
    assert cars.str_reverse() == '[tesla, mazda, trabant, skoda]'
    cars.insert_at_begin("toyota")
    assert str(cars) == '[toyota, skoda, trabant, mazda, tesla]'
    assert cars.str_reverse() == '[tesla, mazda, trabant, skoda, toyota]'

    print("Level 3: OK")

if LEVEL >= 4:
# Testy, level 4
# mazání na konci seznamu

    assert cars.delete_at_end() == 'tesla'
    assert str(cars) == '[toyota, skoda, trabant, mazda]'
    assert cars.str_reverse() == '[mazda, trabant, skoda, toyota]'

    assert cars.delete_at_end() == 'mazda'
    assert str(cars) == '[toyota, skoda, trabant]'
    assert cars.str_reverse() == '[trabant, skoda, toyota]'

    assert cars.delete_at_begin() == 'toyota'
    assert str(cars) == '[skoda, trabant]'
    assert cars.str_reverse() == '[trabant, skoda]'

    assert cars.delete_at_end() == 'trabant'
    assert str(cars) == '[skoda]'
    assert cars.str_reverse() == '[skoda]'

    assert cars.delete_at_end() == 'skoda'
    assert str(cars) == '[]'
    assert cars.str_reverse() == '[]'

    print("Level 4: OK")

if LEVEL >= 5:
# Testy, level 5
# mazání uprostřed seznamu pomocí delete_data(data)

    drinks = DoublyLinkedList()
    drinks.insert_at_begin('limo')
    drinks.insert_at_begin('pivo')
    drinks.insert_at_begin('voda')
    drinks.insert_at_begin('dzus')
    drinks.insert_at_begin('limo')

    assert str(drinks) == '[limo, dzus, voda, pivo, limo]'
    drinks.delete_data('caj')
    assert str(drinks) == '[limo, dzus, voda, pivo, limo]'
    drinks.delete_data('limo')
    assert str(drinks) == '[dzus, voda, pivo, limo]'
    assert drinks.str_reverse() == '[limo, pivo, voda, dzus]'
    drinks.delete_data('pivo')
    assert str(drinks) == '[dzus, voda, limo]'
    assert drinks.str_reverse() == '[limo, voda, dzus]'
    drinks.delete_data('dzus')
    assert str(drinks) == '[voda, limo]'
    assert drinks.str_reverse() == '[limo, voda]'
    drinks.delete_data('limo')
    assert str(drinks) == '[voda]'
    assert drinks.str_reverse() == '[voda]'
    drinks.delete_data('voda')
    assert str(drinks) == '[]'
    assert drinks.str_reverse() == '[]'
    drinks.delete_data('voda')
    assert str(drinks) == '[]'
    assert drinks.str_reverse() == '[]'

    print("Level 5: OK")

if LEVEL >= 6:
# Testy, level 6
# metoda empty() a clear()

    odd = DoublyLinkedList()
    even = DoublyLinkedList()

    assert odd.empty() == True
    assert even.empty() == True

    for i in range(5):
        odd.insert_at_begin(2*i+1)
        even.insert_at_begin(2*i + 2)
    assert str(odd) == '[9, 7, 5, 3, 1]'
    assert str(even) == '[10, 8, 6, 4, 2]'

    assert odd.empty() == False
    assert even.empty() == False

    while not odd.empty():
        odd.delete_at_begin()

    even.clear()
    assert odd.empty() == True
    assert even.empty() == True

    assert odd.str_reverse() == '[]'
    assert even.str_reverse() == '[]'

    print("Level 6: OK")

if LEVEL >= 7:
# Testy, level 7
# metoda contains(data)

    animals = DoublyLinkedList()
    animals.insert_at_begin('pes')
    animals.insert_at_begin('kocka')
    animals.insert_at_begin('jezevec')
    animals.insert_at_begin('meduza')

    assert animals.contains('pes') == True
    assert animals.contains('meduza') == True
    assert animals.contains('slon') == False

    print("Level 7: OK")

if LEVEL >= 8:
# Testy, level 8
# metoda sort(asc)

    assert str(animals) == '[meduza, jezevec, kocka, pes]'
    animals.sort()
    assert str(animals) == '[jezevec, kocka, meduza, pes]'
    assert animals.str_reverse() == '[pes, meduza, kocka, jezevec]'

    animals.sort(False)
    assert str(animals) == '[pes, meduza, kocka, jezevec]'
    assert animals.str_reverse() == '[jezevec, kocka, meduza, pes]'

    test = DoublyLinkedList()
    test.sort()
    assert str(test) == '[]'

    test.insert_at_begin(1)
    test.sort()
    assert str(test) == '[1]'

    print("Level 8: OK")
