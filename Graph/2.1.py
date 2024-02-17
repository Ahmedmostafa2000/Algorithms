#python3

# from sys import setrecursionlimit
#
# setrecursionlimit(10**6)
#




def explore(index,nn,end=[],dead_end=set()):
    print(index,nn[index],end)
    for vertex in nn[index]:
        if vertex in end:
            return 1
        if vertex in dead_end:
            return
        end.append(vertex)
        print(len(nn[vertex-1]))
        if len(nn[vertex-1]) == 0 :
            dead_end.add(vertex)
            end.pop()
            return
        explore(vertex-1,nn,end)




V,E = map(int,input().split())
courses = []
nn = []
for i in range(E):
    courses.append(list(map(int,input().split())))
for i in range(V):
    nn.append(set())

# cycle = set()


for i in range(E):
    nn[courses[i][0]-1].add(courses[i][1])
print(nn)
for i in range(V):
    if explore(i,nn):
        print(1)
        exit()
print(0)
# print(explore(0,nn,cycle))
# print(cycle)
# if set() in nn:
#     print(0)
# else:
#     print(1)
#

