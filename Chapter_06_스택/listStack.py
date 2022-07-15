class ListStack:
    def __init__(self):
        self.__stack = []
    
    def push(self, item):
        self.__stack.append(item)
    
    def pop(self):
        return self.__stack.pop()
    
    def top(self):
        if self.is_empty():
            return None
        else:
            return self.__stack[-1]
    
    def is_empty(self) -> bool:
        return not bool(self.__stack)
    
    def pop_all(self):
        self.__stack.clear()
    
    def print_stack(self):
        print("Stack from top:", end = ' ')
        for index in range(len(self.__stack) - 1, -1, -1):
            print(self.__stack[index], end = ' ')
        print()