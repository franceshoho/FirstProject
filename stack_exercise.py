# put your python code here
from collections import deque

def check_balance(string):
    stack = deque()
    for i in range(len(string)) :
        ch = string[i]
        if (ch == '(') :
            stack.append(ch)
        elif ch == ')' :
            # if stack is empty
            if len(stack) == 0:
                return ("ERROR")
            # if stack isn't empty, see if top = '('
            top = stack.pop()
            if top != '(':
                return ("ERROR")

    if (len(stack) == 0) :
        # if stack after all operations is empty, then correct
        return ("OK")
    else :  # if not empty
        return ("ERROR")

def main():
    string = input()
    print(check_balance(string))


if __name__ == '__main__' :
    main()
