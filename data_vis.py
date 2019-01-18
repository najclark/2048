import os
import matplotlib.pyplot as plt
from statistics import mean
import numpy as np

#random data
all_files = os.listdir(os.path.join('data', 'random_data'))

scores = []

for f in all_files:
    score = int(f.split('-')[0])
    scores.append(score)

print(mean(scores))
plt.hist(scores, bins=10)
plt.show()
