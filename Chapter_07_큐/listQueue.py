class ListQueue:
    def __init__(self):
        self.__queue = []
    
    def enqueue(self, item):
        self.__queue.append(item)
    
    def dequeue(self):
        return self.__queue.pop(0)
    
    def front(self):
        if self.is_empty():
            return None
        else:
            return self.__queue[0]
    
    def is_empty(self) -> bool:
        return not bool(self.__queue)
    
    def dequeue_all(self):
        self.__queue = []
    
    def print_queue(self):
        print("Queue from front:", end = " ")
        for index in range(len(self.__queue)):
            print(self.__queue[index], end = " ")
        print()
