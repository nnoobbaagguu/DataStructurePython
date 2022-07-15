from listNode import ListNode

class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode('dummy', None)
        self.__tail.next = self.__tail
        self.__num_items = 0
    
    def insert(self, index: int, new_item) -> None:
        if index >= 0 and index <= self.__num_items:
            prev = self.get_node(index - 1)
            new_node = ListNode(new_item, prev.next)
            prev.next = new_node
            if index == self.__num_items:
                self.__tail = new_node
            self.__num_items += 1
        else:
            print("index", index, ": out of bound in insert()")
    
    def append(self, new_item) -> None:
        new_node = ListNode(new_item, self.__tail.next)
        self.__tail.next = new_node
        self.__tail = new_node
        self.__num_items += 1
    
    def pop(self, *args):
        if self.is_empty():
            return None
        if len(args) != 0:
            index = args[0]
        if len(args) == 0 or index == -1:
            index = self.__num_items - 1
        if index >= 0 and index <= self.__num_items - 1:
            prev = self.get_node(index - 1)
            ret_item = prev.next.item
            prev.next = prev.next.next
            if index == self.__num_items - 1:
                self.__tail = prev
            self.__num_items -= 1
            return ret_item
        else:
            return None
    
    def remove(self, item):
        (prev, curr) = self.__find_node(item)
        if curr != None:
            prev.next = curr.next
            if curr == self.__tail:
                self.__tail = prev
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
            cnt += 1
        return -2
    
    def is_empty(self) -> bool:
        return self.__num_items == 0
    
    def size(self) -> int:
        return self.__num_items
    
    def clear(self):
        self.__tail = ListNode('dummy', None)
        self.__tail.next = self.__tail
        self.__num_items = 0
    
    def count(self, item) -> int:
        cnt = 0
        for element in self:
            if element == item:
                cnt += 1
        return cnt
    
    def extend(self, iterable):
        for item in iterable:
            self.append(item)
    
    def copy(self) -> b'CircularLinkedList':
        circular_linked_list = CircularLinkedList()
        for element in self:
            circular_linked_list.append(element)
        return circular_linked_list
    
    def reverse(self):
        prev = self.__tail
        curr = prev.next
        head = curr.next
        while curr != self.__tail:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        curr.next = prev
        self.__tail = head

    def sort(self) -> None:
        temp_list = []
        for element in self:
            temp_list.append(element)
        temp_list.sort()
        self.clear()
        self.extend(temp_list)
    
    def __find_node(self, item) -> tuple[ListNode, ListNode]:
        head = prev = self.__tail.next
        curr = prev.next
        while curr != head:
            if curr.item == item:
                return (prev, curr)
            else:
                prev = curr; curr = curr.next
        return (None, None)
    
    def get_node(self, index: int) -> ListNode:
        curr = self.__tail.next
        for _index in range(index + 1):
            curr = curr.next
        return curr
    
    def print_list(self) -> None:
        for element in self:
            print(element, end = " ")
        print()
    
    def __iter__(self):
        return CircularLinkedListIterator(self)

class CircularLinkedListIterator:
    def __init__(self, circular_linked_list):
        self.__head = circular_linked_list.get_node(-1)
        self.iter_position = self.__head.next
    
    def __next__(self):
        if self.iter_position == self.__head:
            raise StopIteration
        else:
            item = self.iter_position.item
            self.iter_position = self.iter_position.next
            return item