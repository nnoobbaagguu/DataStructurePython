from listNode import ListNode

class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__num_items = 0

    def insert(self, index: int, new_item):
        if index >= 0 and index <= self.__num_items:
            prev = self.__get_node(index - 1)
            new_node = ListNode(new_item, prev.next)
            prev.next = new_node
            self.__num_items += 1
        else:
            print("index", index, ": out of bound in insert()")
    
    def append(self, new_item):
        prev = self.__get_node(self.__num_items - 1)
        new_node = ListNode(new_item, prev.next)
        prev.next = new_node
        self.__num_items += 1
    
    def pop(self, index: int):
        if index >= 0 and index <= self.__num_items - 1:
            prev = self.__get_node(index - 1)
            curr = prev.next
            prev.next = curr.next
            self.__num_items -= 1
            return curr.item
        else:
            return None
    
    def remove(self, item):
        (prev, curr) = self.__find_node(item)
        if curr != None:
            prev.next = curr.next
            self.__num_items -= 1
            return item
        else:
            return None
    
    def get(self, index: int):
        if self.is_empty():
            return None
        if index >= 0 and index <= self.__num_items - 1:
            return self.__get_node(index).item
        else:
            return None
    
    def index(self, item):
        curr = self.__head.next
        for _index in range(self.__num_items):
            if curr.item == item:
                return _index
            curr = curr.next
        return -2
    
    def is_empty(self) -> bool:
        return self.__num_items == 0
    
    def size(self) -> int:
        return self.__num_items
    
    def clear(self):
        self.__head = ListNode('dummy', None)
        self.__num_items = 0
    
    def count(self, item) -> int:
        curr = self.__head.next
        _count = 0
        while curr != None:
            if curr.item == item:
                _count += 1
            curr = curr.next
        return _count
    
    def extend(self, linked_list_basic):
        for index in range(linked_list_basic.size()):
            self.append(linked_list_basic.get(index))
    
    def copy(self):
        linked_list_basic = LinkedListBasic()
        for index in range(self.__num_items):
            linked_list_basic.append(self.get(index))
        return linked_list_basic
    
    def reverse(self):
        linked_list_basic = LinkedListBasic()
        for index in range(self.__num_items):
            linked_list_basic.insert(0, self.get(index))
        self.clear()
        for index in range(linked_list_basic.size()):
            self.append(linked_list_basic.get(index))
    
    def sort(self) -> None:
        temp_list = []
        for index in range(self.__num_items):
            temp_list.append(self.get(index))
        temp_list.sort()
        self.clear()
        for index in range(len(temp_list)):
            self.append(temp_list[index])
    
    def __find_node(self, item) -> tuple[ListNode, ListNode]:
        prev = self.__head
        curr = prev.next
        while curr != None:
            if curr.item == item:
                return (prev, curr)
            prev = curr
            curr = curr.next
        return (None, None)

    def __get_node(self, index: int) -> ListNode:
        curr = self.__head
        for _ in range(index + 1):
            curr = curr.next
        return curr

    def print_list(self):
        curr = self.__head.next
        while curr != None:
            print(curr.item, end = " ")
            curr = curr.next
        print()
