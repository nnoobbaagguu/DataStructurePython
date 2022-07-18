from _circularLinkedList import *

class LinkedQueue:
    def __init__(self):
        self.__queue = CircularLinkedList()
    
    def enqueue(self, item):
        self.__queue.append(item)
    
    def dequeue(self):
        return self.__queue.pop(0)
    
    def front(self):
        return self.__queue.get(0)
    
    def is_empty(self):
        return self.__queue.is_empty()
    
    def dequeue_all(self):
        self.__queue.clear()
    
    def print_queue(self):
        print("Queue from front:", end = ' ')
        self.__queue.print_list()