class Heap:
    def __init__(self, _list):
        if _list == None:
            self.__heap_list = []
        else:
            self.__heap_list = _list
    
    def insert(self, element):
        index = len(self.__heap_list)
        self.__heap_list.append(element)
        parent = (index - 1) // 2
        
        while parent >= 0:
            if element > self.__heap_list[parent]:
                self.__heap_list[parent], self.__heap_list[index] = element, self.__heap_list[parent]
                index = parent
                parent = (parent - 1) // 2
            else:
                break
    
    def insert_recursion(self, element):
        self.__heap_list.append(element)
        self.percolate_up(len(self.__heap_list) - 1)
    
    def percolate_up(self, index: int):
        parent = (index - 1) // 2
        if index > 0 and self.__heap_list[index] > self.__heap_list[parent]:
            self.__heap_list[parent], self.__heap_list[index] = self.__heap_list[index], self.__heap_list[parent]
            self.percolate_up(parent)
    
    def delete_max(self):
        if self.is_empty():
            return None
        else:
            max = self.__heap_list[0]
            self.__heap_list[0] = self.__heap_list.pop()
            self.percolate_down(0)
            return max
    
    def percolate_down(self, index: int):
        child = index * 2 + 1
        right = child + 1
        if child < len(self.__heap_list):
            if right < len(self.__heap_list) and self.__heap_list[child] < self.__heap_list[right]:
                child = right
            if self.__heap_list[child] > self.__heap_list[index]:
                self.__heap_list[child], self.__heap_list[index] = self.__heap_list[index], self.__heap_list[child]
                self.percolate_down(child)
    
    def build_heap(self):
        for index in range((len(self.__heap_list) - 1) // 2 , -1, -1):
            self.percolate_down(index)
    
    def max(self):
        return self.__heap_list[0]
    
    def is_empty(self):
        return not bool(self.__heap_list)
    
    def clear(self):
        self.__heap_list.clear()