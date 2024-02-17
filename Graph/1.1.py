#python3
from sys import setrecursionlimit
#setrecursionlimit(10**6)
from sys import stdin
visited = {}

explored = set()

def explore(v,end,start):
    if end in explored:
        return
    for i in visited[v]:
        if not i in explored:
            explored.add(i)
            explore(i,end,start)




maze = stdin.readlines()
V, E = map(int, maze[0].split()[0:2])
for i in range(1, len(maze)-1):
    maze[i] = list(map(int, maze[i].split()[0:2]))
start, end = map(int, maze[-1].split()[0:2])

for i in range(1,V+1):
    visited[i]=set()
for i in range(1,len(maze)-1):
    visited[maze[i][0]].add(maze[i][1])
    visited[maze[i][1]].add(maze[i][0])


explore(start,end,start)
if end in explored:
    print(1)
else:
    print(0)

