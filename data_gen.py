from AI2048 import Game
import secrets
import os
from tqdm import tqdm
import numpy as np
import time

MAX_TURNS = 100
SAVE_THRESHOLD = 3000
path = os.path.join('data', 'random_data')
iterations = 1000000
saves_made = 0

for i in tqdm(range(iterations)):
    game = Game()
    record = []
    while game.game_over is False:
        # direction = int(input("Direction: "))
        direction = secrets.choice([0, 1, 2, 3])

        grid = game.grid
        linear = []
        for r in grid:
            linear += r
        dir = [0, 0, 0, 0]
        dir[direction] = 1
        record.append([linear, dir])

        game.slide(direction)

    if game.score > SAVE_THRESHOLD:
        saves_made += 1
        filename = f"{game.score}-{int(time.time()*1000)}.npy"
        np.save(f"{os.path.join(path, filename)}", record)

print(f"{saves_made/iterations*100}% of the games played met the save_threshold:{SAVE_THRESHOLD} and were saved.")
