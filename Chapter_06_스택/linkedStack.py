from ..Chapter_05_리스트.linkedListBasic import LinkedListBasic

class LinkedStack:
    def __init__(self):
        self.__list = LinkedListBasic()
    
    def push(self, item):
        self.__list.insert(0, item)
    
    def pop(self):
        return self.__list.pop(0)
    
    def top(self):
        if self.is_empty():
            return None
        else:
            return self.__list.get(0)
    
    def is_empty(self):
        return self.__list.is_empty()
    
    def pop_all(self):
        self.__list.clear()
    
    def print_stack(self):
        print("Stack from top:", end = " ")