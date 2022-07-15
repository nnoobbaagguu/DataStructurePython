from bidirectNode import *

class CircularDoublyLinkedList:
    def __init__(self):
        self.__head = BidirectNode('dummy', None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__num_items = 0
    
    def insert(self, index: int, new_item) -> None:
        if index >= 0 and index <= self.__num_items:
            prev = self.get_node(index - 1)
            new_node = BidirectNode(new_item, prev, prev.next)
            prev.next.prev = new_node
            prev.next = new_node
            self.__num_items += 1
    
    def append(self, new_item) -> None:
        prev = self.__head.prev
        new_node = BidirectNode(new_item, prev, self.__head)
        prev.next.prev = new_node
        prev.next = new_node
        self.__num_items += 1

    def pop(self, *args):
        if self.is_empty():
            return None
        if len(args) != 0:
            index = args[0]
        if len(args) == 0 or index == -1:
            index = self.__num_items - 1
        if index >= 0 and index <= self.__num_items - 1:
            curr = self.get_node(index)
            ret_item = curr.item
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__num_items -= 1
            return ret_item
        else:
            return None

    def remove(self, item):
        curr = self.__find_node(item)
        if curr != None:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__num_items -= 1
            return item
        else:
            return None
    
    def get(self, *args):
        if self.is_empty():
            return None
        if len(args) != 0:
            index = args[0]
        if len(args) == 0 or index == -1:
            index = self.__num_items - 1
        if index >= 0 and index <= self.__num_items - 1:
            return self.get_node(index).item
        else:
            return None
    
    def index(self, item) -> int:
        cnt = 0
        for element in self:
            if element == item:
                return cnt
            else:
                cnt += 1
        return -2
    
    def is_empty(self):
        return self.__num_items == 0
    
    def size(self) -> int:
        return self.__num_items
    
    def clear(self):
        self.__head = BidirectNode('dummy', None, None)
        self.__head.next = self.__head
        self.__head.prev = self.__head
        self.__num_items = 0
    
    def count(self, item):
        cnt = 0
        for element in self:
            if element == item:
                cnt += 1
        return cnt
    
    def extend(self, iterable):
        for element in iterable:
            self.append(element)
    
    def copy(self) -> 'CircularDoublyLinkedList':
        circular_doubly_linked_list = CircularDoublyLinkedList()
        for element in self:
            circular_doubly_linked_list.append(element)
        return circular_doubly_linked_list
    
    def reverse(self) -> None:
        prev = self.__head
        curr = prev.next
        prev.next, prev.prev = prev.prev, prev.next
        prev = curr; curr = curr.next
        for _ in range(self.__num_items):
            prev.next, prev.prev = prev.prev, prev.next
            prev = curr; curr = curr.next
    
    def sort(self) -> None:
        temp_list = []
        for element in self:
            temp_list.append(element)
        temp_list.sort()
        self.clear()
        for element in temp_list:
            self.append(element)
    
    def __find_node(self, item) -> BidirectNode:
        curr = self.__head.next
        while curr != self.__head:
            if curr.item == item:
                return curr
            else:
                curr = curr.next
        return None
    
    def get_node(self, index: int) -> BidirectNode:
        curr = self.__head
        for _ in range(index + 1):
            curr = curr.next
        return curr
    
    def print_list(self) -> None:
        for element in self:
            print(element, end = " ")
        print()

    def __iter__(self):
        return CircularDoublyLinkedListIterator(self)


class CircularDoublyLinkedListIterator:
    def __init__(self, circular_doubly_linked_list):
        self.__head = circular_doubly_linked_list.get_node(-1)
        self.iter_position = self.__head.next
    
    def __next__(self):
        if self.iter_position == self.__head:
            raise StopIteration
        else:
            item = self.iter_position.item
            self.iter_position = self.iter_position.next
            return item