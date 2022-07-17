from listStack import *

def evaluate(post):
    s = ListStack()
    digit_previously = False
    for index in range(len(post)):
        ch = post[index]
        if ch.isdigit():
            if digit_previously:
                s.push(s.pop() * 10 + int(ch))
            else:
                s.push(int(ch))
                digit_previously = True
        elif is_operator(ch):
            s.push(operation(s.pop(), s.pop(), ch))
            digit_previously = False
        else:
            digit_previously = False
    return s.pop()   

def is_operator(ch) -> bool:
    return ch == '+' or ch == '/' or ch == '-' or ch == '*'

def operation(operand2: int, operand1: int, operator) -> int:
    return {'+': operand1 + operand2, '-': operand1 - operand2, '*': operand1 * operand2, '/': operand1 / operand2}[operator]

def main():
    postfix = "700 3 47 + 6 * - 4 /"
    print("Input string:", postfix)
    answer = evaluate(postfix)
    print("Answer: ", answer)

if __name__ == '__main__':
    main()