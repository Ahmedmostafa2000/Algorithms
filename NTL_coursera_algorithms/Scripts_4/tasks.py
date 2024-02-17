from random import sample,seed,shuffle
from itertools import cycle
seed(42)
videos = sample(range(9,25),15)
video3 = cycle(videos)
team = ["Hassan", "Akram", "Shady", "Ahmad", "Gamal"]
shuffle(team)
with open('out.txt', 'w') as f:
    for i in range(5):
        f.write(str(team[i]))
        f.write('\t\t')
        for j in range(3):
            f.write(str(next(video3)))
            f.write('\t')
        f.write('\n')
    f.close()




