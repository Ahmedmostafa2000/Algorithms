#python3
class Stack:
    def __init__(self):
        self.stack =[]
        self.been = 0

    def push(self,item):
        self.stack.append(item)
        self.been += 1

    def pop(self):
        if self.is_empty():
            return None
        self.stack.pop(-1)

    def __str__(self):
        return str(self.stack)




    def is_empty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]


x = input()
stack = Stack()
success = True
if (len(x) == 1) or (x[0] in [')',"]",'}']) :
    print(1)
    exit()
for i in range(len(x)):
    wrong = i
    if x[i] in ['(','[','{']:
        stack.push(x[i])
    elif x[i] in [')',"]",'}']:
        top = stack.top()
        if (top == '(' and x[i] != ')')\
            or (top == '[' and x[i] != ']')\
            or (top == '{' and x[i] != '}')\
            or (top == None):
            success = False
            break
        else:
            stack.pop()

if not stack.is_empty():
    pass
elif success:
    print('Success')
    exit()
print(wrong+1)
