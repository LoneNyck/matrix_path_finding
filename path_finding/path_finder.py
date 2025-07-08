from collections import deque

def get_matrix(file_name: str) -> list:
    matrix = []
    try:
        with open(file_name, "r") as f:
            for line in f:
                matrix.append(line.strip())
        
        return matrix
    except FileNotFoundError:
        print("Couldn't find the file path")
        return None

def find_path(mat: list, visited: list, queue: deque, parent: dict) -> tuple:
    if len(queue) == 0:
        print("No path has been found")
        return None, None
    
    (x, y) = queue[0]
    
    if(mat[x][y]) == 'E':
        print(f"\nExit has been found, coord ({x}, {y})!\n")
        return x, y
    
    queue.popleft()
    
    if y > 0 and mat[x][y - 1] != '#' and not visited[x][y - 1]:
        queue.appendleft((x, y - 1))
        parent[(x, y - 1)] = (x, y)
        visited[x][y - 1] = True
        
    if x > 0 and mat[x - 1][y] != '#' and not visited[x - 1][y]:
        queue.appendleft((x - 1, y))
        parent[(x - 1, y)] = (x, y)
        visited[x - 1][y] = True
    
    if y + 1 < len(mat[0]) and mat[x][y + 1] != '#' and not visited[x][y + 1]:
        queue.appendleft((x, y + 1))
        parent[(x, y + 1)] = (x, y)
        visited[x][y + 1] = True
    
    if x + 1 < len(mat) and mat[x + 1][y] != '#' and not visited[x + 1][y]:
        queue.appendleft((x + 1, y))
        parent[(x + 1, y)] = (x, y)
        visited[x + 1][y] = True

    return find_path(mat, visited, queue, parent)

file_name = str(input("Enter matrix file name: "))

matrix = get_matrix(file_name)

try: 
    visited = [[False for _ in line] for line in matrix]

    parent = {} # save the parent of each node to build the path
    queue = deque([])

    for line in matrix:
        for el in line:
            if matrix[matrix.index(line)][line.index(el)] == 'S':
                start_x = matrix.index(line)
                start_y = line.index(el)
                break

    queue.append((start_x, start_y))
    visited[start_x][start_y] = True

    print("")
    for line in matrix:
        for el in line:
            if el == '0':
                print(' ', end = ' ')
            else:
                print(el, end = ' ')
        print("")

    exit_x, exit_y = find_path(matrix, visited, queue, parent)
    queue.clear()

    path = []
    current = (exit_x, exit_y)
    while current in parent:
        path.append(current)
        current = parent[current]
        
    path.append((start_x, start_y))
    path.reverse()

    print("Printing the path: ")
    for step in path:
        if step == (start_x, start_y):
            print("START",  end = '->')
            
        if path.index(step) + 1 < len(path):
            if path[(path.index(step) + 1)][0] > path[path.index(step)][0]:
                print("down", end = '->')
            elif path[(path.index(step) + 1)][0] < path[path.index(step)][0]:
                print("up", end = '->')
            elif path[path.index(step) + 1][1] > path[path.index(step)][1]:
                print("right", end = '->')
            elif path[path.index(step) + 1][1] < path[path.index(step)][1]:
                print("left", end = '->')
        else:
            print("END")
            
except TypeError:
    print("Code has therefore come to an unexpected error")