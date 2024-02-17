from math import log2
class BinaryTree:
    def __init__(self,tree):
        self.tree = tree

    def parent(self,index):
        return (index-1)//2

    def child1(self,index):
        if len(self.tree)<=index*2:
            return
        return index*2+1

    def child2(self,index):
        if len(self.tree) <= index*2:
            return
        return index*2+2


    def shift_up(self,index):
        while index>0 and self.tree[self.parent(index)]<self.tree[index]:
            self.tree[self.parent(index)], self.tree[index] =\
                self.tree[index], self.tree[self.parent(index)]

            index = self.parent(index)

    def __str__(self,by_level=False):
        if by_level:
            string = ''
            spacing = len(str(max(self.tree)))
            level = int(log2(len(self.tree)))

            for j in range(level):
                #string+=' '*int(spacing*((len(self.tree)//2-4)-2**(j-1)))
                for i in range(2**j-1,2**(j+1)-1):
                    string+=str(self.tree[i])
                    string+=' '*spacing
                string+='\n'
            return string
        return str(self.tree)

from random import randint,seed
y = []
for i in range(32):
    y.append(randint(0,9))
y[14]=11
x = BinaryTree(y)
print(x.__str__(True))
x.shift_up(14)
print(x.__str__(True))