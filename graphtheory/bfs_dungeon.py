# Dungeon problem statement
#  the dungeon has a size of R x C and you start at cell 'S' and there's an exit at cell 'E'.
#  a cell full of rock is indicated by a '#' and empty cells are represented by a '.'
#  ------------C-------------
#  |   S  .  .  #  .  .  .  |
#  |   .  #  .  .  .  #  .  |
#  R   .  #  .  .  .  .  .  |
#  |   .  .  #  #  .  .  .  |
#  |   #  .  #  E  .  #  .  |
#  --------------------------
#
#  for this case, use one queue for each dimension is the better approach than one queue pack/unpack coordinates.
#  the thing that needs to be aware is that the queues enqueue/dequeue needs to be in sync in each dimension.

# the dungeon
m = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '#', 'E', '.', '#', '.']
]

R = len(m)
C = len(m[0])

# 'S' symbol row and column
sr = 0
sc = 0

# direction vector technique
# North, south, east, west
dr = [-1, +1,  0,  0]
dc = [0,  0,  +1, -1]

# row queue
rq = []
# column queue
cq = []

visited = [[False for i in range(C)] for j in range(R)]
prev = [[None for i in range(C)] for j in range(R)]

reach_end = False
# end row/column
er = -1
ec = -1

# at least 1 (current one)
nodes_left_in_layer = 1
nodes_in_next_layer = 0
move_count = 0


def explore_neighbors(r, c):
    global nodes_in_next_layer, prev, visited
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        # bound check
        if rr < 0 or cc < 0:
            continue
        if rr >= R or cc >= C:
            continue

        # skip visited locations or blocked cells
        if visited[rr][cc]:
            continue
        if m[rr][cc] == '#':
            continue

        rq.insert(0, rr)
        cq.insert(0, cc)
        visited[rr][cc] = True
        prev[rr][cc] = [r, c]
        nodes_in_next_layer = nodes_in_next_layer + 1


def solve(sr, sc):
    global nodes_left_in_layer, nodes_in_next_layer, move_count, er, ec

    rq.insert(0, sr)
    cq.insert(0, sc)
    visited[sr][sc] = True

    while len(rq) > 0:   # or len(cq) > 0
        r = rq.pop()
        c = cq.pop()
        if m[r][c] == 'E':
            reach_end = True
            er = r
            ec = c
            break
        explore_neighbors(r, c)
        nodes_left_in_layer = nodes_left_in_layer - 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count = move_count + 1

    if reach_end:
        return move_count
    return -1


def reconstructPath():
    # Reconstruct path going backward from e
    path = []
    at = [er, ec]
    while(prev[at[0]][at[1]] != None):
        at = prev[at[0]][at[1]]
        path.append(at)
    path.reverse()

    if len(path) > 0 and path[0] == [sr, sc]:
        return path
    return []


def bfs():
    result_move_count = solve(sr, sc)
    print('steps:' + str(result_move_count))
    if result_move_count > 0:
        return reconstructPath()


print(bfs())
