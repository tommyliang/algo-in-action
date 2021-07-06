# given a graph and a starting node and a target node,
# find a path between them if exist
# n = number of nodes in the graph
# g = ajacency list representing unweighted graph

def solve(g, s):
    # q = queue data structure with enqueue and dequeue
    q = []
    q.insert(0, s)
    n = len(g)

    visited = [False for i in range(n)]
    visited[s] = True

    prev = [None for i in range(n)]
    while len(q) > 0:
        node = q.pop()

        for next in g[node]:
            if not visited[next]:
                q.insert(0, next)
                visited[next] = True
                prev[next] = node
    return prev


def reconstructPath(s, e, prev):
    # Reconstruct path going backward from e
    path = []
    at = e
    while(prev[at] != None):
        at = prev[at]
        path.append(at)
    path.reverse()

    if len(path) > 0 and path[0] == s:
        return path
    return []


def bfs(g, s,  e):
    prev = solve(g, s)

    return reconstructPath(s, e, prev)


g = [
    # 0
    [7, 9, 11],
    # 1
    [],
    # 2
    [],
    # 3
    [2, 4],
    # 4
    [],
    # 5
    [],
    # 6
    [5],
    # 7
    [3, 6, 11],
    # 8
    [1, 12],
    # 9
    [8, 10],
    # 10
    [1],
    # 11
    [],
    # 12
    [2]
]

print(bfs(g, 0, 4))  # [0, 7, 3]
print(bfs(g, 0, 5))  # [0, 9, 6]
print(bfs(g, 7, 12))  # []
