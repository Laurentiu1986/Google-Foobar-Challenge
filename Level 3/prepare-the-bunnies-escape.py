
  
'''
Function to test if a cell is valid by test its existence and if the cell fit in our matrix.
Also, if the cell was already visited, we return False
'''
def isValid(map, visited, row, col, m, n):
    if (row >= 0) and (row < m) and (col >= 0) and (col < n) and map[row][col]==0 and not visited[row][col]:
        return True
    return False

'''
Breadth first search function, where we search for every neighbour of every cell from our matrix.
We start by append the first cell (0, 0) into the queue (a list in my case) and search for its neighbours.
When we find them and test if the cells are valid, we append them into our queue and also we increase the distance.
In the next steps, we pop from the left (front) of our queue the oldest element introduced and check for its neighbours as well.
If a neighbour already exists in queue, we skip.
We'll doing this until the queue is empty, meaning that there is no path, or until we reach the destination and check for coordinates.

'''
def bfs(map, i, j, x, y, row, col):
    visited = [[False] * (y+1) for i in range(x+1)]
    i = j = 0

    #lista = deque()
    lista = []
    node = []
    done = False
    
    visited[i][j] = True
    lista.append([i, j, 0])
    min_dist = 1

    while(len(lista) > 0):
        node = lista.pop(0)

        i = node[0]
        j = node[1]
        dist = node[2]

        if i == x and j == y:
            min_dist = dist
            done = True
            break
        
        for k in xrange(4):
            # print("i: ", i, " j: ", j, " row: ", row[k], " col[k]: ", col[k])
            # print(" k----", k, " |", i + row[k], j + col[k], len(map), len(map[0]))
            if isValid(map, visited, i + row[k], j + col[k], len(map), len(map[0])):
                visited[i + row[k]][j + col[k]] = True
                lista.append([i + row[k], j + col[k], dist + 1])
                # print("Lista: ", lista)
    
    '''
    the purpose for this extra-check is that in some cases, we can't reach any destination and we are blocked into the matrix.
    In that way, the function will return the value increased until the block, which always be lower than our minimum steps 
    we need to make to reach a destination. (For example, if we have a matrix of 5x5, the minimum path will be 5+5-2 = 8).
    So the solution was to return value '1000', a random higher value that we do not expect to reach in our test cases (max matrix dimensions is 20).
    This will help us to find the minimum between bfs function and break_wall function, which return a list of minimum paths.
    
    '''
    if done:
        return min_dist+1
    else:
        return 1000        


'''
The break_wall function is checking for every '1' in the matrix and replace with a '0'. 
Then, we execute the bfs function using an alternative copy of the matrix, but with the value replaced.
After the execution, we append the value into a list and follow the same algorithm with the rest of 1's.
The function return the list and finally we will compare this list with the value returned from the main bfs function.
If the min of this list is lower than the value from the bfs function, then we know that a wall break can be done
and return this certain minimum.
'''
def break_wall(map, i, j, x, y, row, col):

    visited = [[False] * (y+1) for i in range(x+1)]
    i = j = 0
    min_list = []
    map_wall = [row[:] for row in map]
    # print(map_wall)
    # print("----------", x, y)
    for x1 in xrange(x+1):
        for y1 in xrange(y+1):
            row = [-1, 0, 0, 1]
            col = [0, -1, 1, 0]
            if map[x1][y1] == 1:
                map_wall[x1][y1] = 0
                # print(map_wall)
                min_list.append(bfs(map_wall, 0, 0, x, y, row, col))
                map_wall[x1][y1] = 1
    return min(min_list)

def solution(map):
    
    
    m = len(map)
    n = len(map[0])
    row = [-1, 0, 0, 1]
    col = [0, -1, 1, 0]

    min_length = m - n - 2

    return min(bfs(map, 0, 0, m-1, n-1, row, col), break_wall(map, 0, 0, m-1, n-1, row, col))




