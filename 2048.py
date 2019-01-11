import secrets

GAME_SIZE = 4
grid = [[0 for x in range(GAME_SIZE)] for y in range(GAME_SIZE)]
score = 0
# grid = [[2, 2, 2, 2], [0, 0, 2, 0], [0, 0, 0, 2], [0, 0, 0, 0]]

def addNumber():
    zeros = []
    for c in range(len(grid)):
        for r in range(len(grid[c])):
            if grid[c][r] == 0:
                zeros.append((c, r))
    if len(zeros) == 0:
        print("Game Over")
        return False
    else:
        pos = secrets.choice(zeros)
        grid[pos[0]][pos[1]] = 4 if (secrets.randbelow(10) < 1) else 2
    return grid

def shift(list, direction):
    zeros = [0 for i in range(list.count(0))]
    shifted = [x for x in list if x != 0]
    if direction == 0:
        shifted = shifted + zeros
    else:
        shifted = zeros + shifted
    return shifted

def combine(direction):
    global score
    good_move = False
    if direction == 1:
        for r in range(len(grid)):
            row = grid[r]
            for i in range(1, len(row))[::-1]:
                if row[i] == row[i-1]:
                    good_move = True
                    row[i] = row[i] + row[i-1]
                    row[i-1] = 0
                    score += row[i]
                    row = shift(row, 1)
                    grid[r] = row
    elif direction == 3:
        for r in range(len(grid)):
            row = grid[r]
            for i in range(len(row)-1):
                if row[i] == row[i+1]:
                    good_move = True
                    row[i] = row[i] + row[i+1]
                    row[i+1] = 0
                    score += row[i]
                    row = shift(row, 0)
                    grid[r] = row
    elif direction == 0:
        for c in range(len(grid[0])):
            col = [grid[r][c] for r in range(len(grid))]
            for i in range(len(col)-1):
                if col[i] == col[i+1]:
                    good_move = True
                    col[i] = col[i] + col[i+1]
                    col[i+1] = 0
                    score += col[i]
                    col = shift(col, 0)
                    for r in range(len(grid)):
                        grid[r][c] = col[r]
    elif direction == 2:
        for c in range(len(grid[0])):
            col = [grid[r][c] for r in range(len(grid))]
            for i in range(1, len(col))[::-1]:
                if col[i] == col[i-1]:
                    good_move = True
                    col[i] = col[i] + col[i-1]
                    col[i-1] = 0
                    score += col[i]
                    col = shift(col, 1)
                    for r in range(len(grid)):
                        grid[r][c] = col[r]

    return good_move


def slide(direction):
    global grid
    if direction == 1 or direction == 3:
        for r in range(len(grid)):
            grid[r] = shift(grid[r], 1 if (direction == 1) else 0)
    elif direction == 0 or direction == 2:
        for c in range(len(grid[0])):
            col = [grid[r][c] for r in range(len(grid))]
            shifted = shift(col, 0 if (direction == 0) else 1)
            for r in range(len(grid)):
                grid[r][c] = shifted[r]
    combine(direction)
    return addNumber()

def grid_print(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            print(grid[r][c], end=' ')
        print()


addNumber()
direction = int(input("Direction: "))
while slide(direction) is not False:
    grid_print(grid)
    print(f"Score: {score}")
    direction = int(input("Direction: "))

# combine(1)
# print(grid)
