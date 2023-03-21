with open('data.txt') as f:
    data = [list(row) for row in f.read().split('\n')]

data2 = data

def state(grid):
    r, c = len(grid), len(grid[0])
    newGrid = [x[:] for x in grid]
    change = False
    for i in range(r):
        for j in range(c):
            if grid[i][j] != '.':
                adj = 0
                adj += i > 0 and j > 0 and grid[i - 1][j - 1] == '#'
                adj += i > 0 and grid[i - 1][j] == '#'
                adj += i > 0 and j + 1 < c and grid[i - 1][j + 1] == '#'
                adj += j > 0 and grid[i][j - 1] == '#'
                adj += j + 1 < c and grid[i][j + 1] == '#'
                adj += i + 1 < r and j > 0 and grid[i + 1][j - 1] == '#'
                adj += i + 1 < r and grid[i + 1][j] == '#'
                adj += i + 1 < r and j + 1 < c and grid[i + 1][j + 1] == '#'

                if grid[i][j] == 'L' and not adj:
                    change = True
                    newGrid[i][j] = '#'
                if grid[i][j] == '#' and adj >= 4:
                    change = True
                    newGrid[i][j] = 'L'
    return newGrid, change


change = True
while change:
    data, change = state(data)

total = 0
for row in data:
    total += row.count('#')
print(total)


data = data2

def canSee(grid, r, c, dr, dc):
    if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]) or grid[r][c] == 'L':
        return False
    if grid[r][c] == '#':
        return True
    return canSee(grid, r + dr, c + dc, dr, dc)


def state(grid):
    r, c = len(grid), len(grid[0])
    newGrid = [[grid[i][j] for j in range(c)] for i in range(r)]
    change = False
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                continue

            adj = 0
            adj += canSee(grid, i - 1, j - 1, -1, -1)
            adj += canSee(grid, i - 1, j, -1, 0)
            adj += canSee(grid, i - 1, j + 1, -1, 1)
            adj += canSee(grid, i, j - 1, 0, -1)
            adj += canSee(grid, i, j + 1, 0, 1)
            adj += canSee(grid, i + 1, j - 1, 1, -1)
            adj += canSee(grid, i + 1, j, 1, 0)
            adj += canSee(grid, i + 1, j + 1, 1, 1)

            if grid[i][j] == 'L' and adj == 0:
                change = True
                newGrid[i][j] = '#'
            elif grid[i][j] == '#' and adj >= 5:
                change = True
                newGrid[i][j] = 'L'

    return newGrid, change


change = True
while change:
    data, change = state(data)

total = 0
for row in data:
    total += row.count('#')
print(total)