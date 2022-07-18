from tokenize import String
from _listStack import *
from listQueue import *

def is_palindrome(string: String) -> bool:
    s = ListStack(); q = ListQueue()
    for index in range(len(string)):
        s.push(string[index])
        q.enqueue(string[index])
    while not s.is_empty():
        if s.pop() != q.dequeue():
            return False
        else:
            continue
    return True

def main():
    print("Palindrome Check!")
    str = 'lioninoil'
    t = is_palindrome(str)
    print(str, "is Palindrome?:", t)

if __name__ == "__main__":
    main()