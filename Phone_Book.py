#python3

class PhoneBook:
    def __init__(self):
        self.p_b = {}

    def add(self,num,name):
        self.p_b[num]=name

    def find(self,num):
        try:
            return self.p_b[num]
        except KeyError:
            return "not found"

    def dele(self,num):
        try:
            del self.p_b[num]
        except KeyError:
            return



# book = PhoneBook()
# book.add(911,"police")
# book.dele(911)
# print(book.p_b)


shell = {0:"add",1:"find",2:"del"}
n = int(input())
book = PhoneBook()
for i in range(n):
    command = input().split()
    if command[0]==shell[0]:
        book.add(command[1],command[2])
    elif command[0]==shell[1]:
        print(book.find(command[1]))
    elif command[0]==shell[2]:
        book.dele(command[1])
'''
12
add 911 police
add 76213 Mom
add 17239 Bob
find 76213
find 910
find 911
del 910
del 911
find 911
find 76213
add 76213 daddy
find 76213
'''