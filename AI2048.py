import secrets
import copy

class Game:
    def __init__(self):
        GAME_SIZE = 4
        self.grid = [[0 for x in range(GAME_SIZE)] for y in range(GAME_SIZE)]
        self.prev_board = [[0 for x in range(GAME_SIZE)] for y in range(GAME_SIZE)]
        self.score = 0
        self.game_over = False
        self.valid_move = True
        self.move_spam = 10
        self.moves = 0
        self.addNumber()
        self.addNumber()


    def all_zeros(self):
        zeros = []
        for c in range(len(self.grid)):
            for r in range(len(self.grid[c])):
                if self.grid[c][r] == 0:
                    zeros.append((c, r))
        return zeros
    #Adds a new number to the board
    #returns whether the game is over
    def addNumber(self):
        zeros = self.all_zeros()
        if len(zeros) == 0:
            print("Game Over")
            self.game_over = True
            return False
        else:
            pos = secrets.choice(zeros)
            self.grid[pos[0]][pos[1]] = 4 if (secrets.randbelow(10) < 1) else 2
            self.game_over = False
        return self.grid

    #Slides all non-zero values of a list to the beginning or end
    #returns new shifted list
    def shift(self, list, direction):
        zeros = [0 for i in range(list.count(0))]
        shifted = [x for x in list if x != 0]
        if direction == 0:
            shifted = shifted + zeros
        else:
            shifted = zeros + shifted
        return shifted

    #Combines adjacent like numbers
    def combine(self, direction):
        if direction == 1:
            for r in range(len(self.grid)):
                row = self.grid[r]
                for i in range(1, len(row))[::-1]:
                    if row[i] == row[i-1]:
                        row[i] = row[i] + row[i-1]
                        row[i-1] = 0
                        self.score += row[i]
                        row = self.shift(row, 1)
                        self.grid[r] = row
        elif direction == 3:
            for r in range(len(self.grid)):
                row = self.grid[r]
                for i in range(len(row)-1):
                    if row[i] == row[i+1]:
                        row[i] = row[i] + row[i+1]
                        row[i+1] = 0
                        self.score += row[i]
                        row = self.shift(row, 0)
                        self.grid[r] = row
        elif direction == 0:
            for c in range(len(self.grid[0])):
                col = [self.grid[r][c] for r in range(len(self.grid))]
                for i in range(len(col)-1):
                    if col[i] == col[i+1]:
                        col[i] = col[i] + col[i+1]
                        col[i+1] = 0
                        self.score += col[i]
                        col = self.shift(col, 0)
                        for r in range(len(self.grid)):
                            self.grid[r][c] = col[r]
        elif direction == 2:
            for c in range(len(self.grid[0])):
                col = [self.grid[r][c] for r in range(len(self.grid))]
                for i in range(1, len(col))[::-1]:
                    if col[i] == col[i-1]:
                        col[i] = col[i] + col[i-1]
                        col[i-1] = 0
                        self.score += col[i]
                        col = self.shift(col, 1)
                        for r in range(len(self.grid)):
                            self.grid[r][c] = col[r]

    #Slides the whold grid in a direction
    def slide(self, direction):
        self.prev_board = copy.deepcopy(self.grid)
        self.valid_move = True

        if direction == 1 or direction == 3:
            for r in range(len(self.grid)):
                self.grid[r] = self.shift(self.grid[r], 1 if (direction == 1) else 0)
        elif direction == 0 or direction == 2:
            for c in range(len(self.grid[0])):
                col = [self.grid[r][c] for r in range(len(self.grid))]
                shifted = self.shift(col, 0 if (direction == 0) else 1)
                for r in range(len(self.grid)):
                    self.grid[r][c] = shifted[r]
        self.combine(direction)

        if self.prev_board == self.grid:
            self.valid_move = False
            # self.score -= round(self.score * 0.1)
            self.move_spam -= 1
        else:
            self.move_spam = 10
            self.moves += 1
            self.addNumber()

        if self.move_spam == 0:
            self.game_over = True

    #prints the grid in the console
    def grid_print(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                print(self.grid[r][c], end=' ')
            print()
