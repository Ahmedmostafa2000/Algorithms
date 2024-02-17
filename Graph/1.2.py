#python3


class Graph:
    def __init__(self,edges,vertices):
        self.E = edges
        self.V = []
        self.islands = None
        for i in range(vertices):
            self.V.append(set())
        self.vnn()
        self.island_make()

    def vnn(self):
        for edge in range(len(self.E)):
            self.V[self.E[edge][0]-1].add(self.E[edge][1])
            self.V[self.E[edge][0] - 1].add(self.E[edge][0])
            self.V[self.E[edge][1]-1].add(self.E[edge][0])
            self.V[self.E[edge][1] - 1].add(self.E[edge][1])

    def island_make(self):
        islands = self.V.copy()
        unique_islands = []
        for i in range(len(self.V)):
            for j in range(i+1,len(self.V)):
                if self.V[i].intersection(self.V[j]):
                    islands[i] = islands[i].union(islands[j])
                    islands[j] = islands[j].union(islands[i])

        for i in range(len(islands)):
            if not islands[i] in unique_islands:
                unique_islands.append(islands[i])
        self.islands = unique_islands


V, E = map(int, input().split())
maze = []

for i in range(E):
    maze.append(list(map(int,input().split())))
x = Graph(maze,V)
count = 0
print(len(x.islands))

# set().in
# from sys import setrecursionlimit
# #setrecursionlimit(10**6)
# from sys import stdin
# visited = {}
#
# explored = {}
# def explore(v,end,start):
#     if end in explored[start]:
#         explored[end]=explored[end].union(explored[start])
#         return
#     for i in visited[v]:
#         if not i in explored[start]:
#             explored[start].add(i)
#             explore(i,end,start)
#
#
#
#
# maze = stdin.readlines()
# V, E = map(int, maze[0].split()[0:2])
# for i in range(1, len(maze)):
#     maze[i] = list(map(int, maze[i].split()[0:2]))
#
# for i in range(1,V+1):
#     visited[i]=set()
#
# for i in range(1,len(maze)):
#     visited[maze[i][0]].add(maze[i][1])
#     visited[maze[i][1]].add(maze[i][0])
# for i in range(1,V+1):
#     explored[i]=set()
#
# for i in range(1,E+1):
#     explore(i,maze[i][0],maze[i][1])
#     #explore(i, maze[i][1], maze[i][0])
# unique = []
#
# for i in explored:
#     for j in explored[i]:
#         explored[j]=explored[j].union(explored[i])
#
# for i in explored.values():
#     if not i in unique:
#         unique.append(i)
# print(len(unique))

"""
5 10 
1 2 
1 3 
4 5 
1 4 
1 5 
2 3 
2 5 
3 4 
2 4 
3 5


4 3 
1 2 
3 2 
4 3

5 10
1 2 
1 3 
4 5 
1 4 
1 5 
2 3 
2 5 
3 4 
2 4 
3 5


100 100 
27 96 
6 9 
81 98 
21 94 
22 68 
76 100 
8 50 
38 86 
71 75 
32 93 
16 50 
71 84 
6 72 
22 58 
7 19 
19 76 
44 75 
24 76 
31 35 
11 89 
42 98 
63 92 
37 38 
20 98 
45 91 
23 53 
37 91 
76 93 
67 90 
12 22 
43 52 
23 56 
67 68 
1 21 
17 83 
63 72 
30 32 
7 91 
50 69 
38 44 
55 89 
15 23 
11 72 
28 42 
22 69 
56 79 
53 58 
5 83 
13 72 
7 93 
20 54 
21 55 
66 89 
2 91 
18 88 
26 64 
11 61 
28 59 
12 86 
42 95 
17 82 
50 66 
66 99 
40 71 
20 40 
5 66 
92 95 
32 46 
7 36 
44 94 
6 31 
19 67 
26 57 
53 84 
10 68 
28 74 
34 94 
25 61 
71 88 
10 89 
28 52 
72 79 
39 73 
11 80 
44 79 
13 77 
30 96 
30 53 
10 39 
1 90 
40 91 
62 71 
44 54 
15 17 
69 74 
13 67 
24 69 
34 96 
21 50 
20 91
"""