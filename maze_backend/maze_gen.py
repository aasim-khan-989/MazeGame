from random import shuffle, randrange
from maze_backend import maze_end_Point
from sys import setrecursionlimit
setrecursionlimit(4000)

def make_maze(w = 3, h = 4):
    """
    This code generates a binary 2D list,
    where 0 is space and 1 is wall.
    the dimension of the produced maze will be
    size = given_width*2-1 X given_height*2-1

    """
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    w_t, h_t = w*2-1,h*2-1
    ver1 = [[1 for __ in range(w_t)] for _ in range(h_t)]
    for j in range(h_t):
        if j%2==0:
            for i in range(w_t):
                if i%2==0: ver1[j][i] = 0
                else:ver1[j][i] = 1

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: ver1[max(y, yy)*2-1][x*2] = 0
            if yy == y: ver1[y*2][max(x, xx)*2-1] = 0
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    ver1 = maze_end_Point.find_end(ver1)
    ver1[0][0] = 2

    print("The new binary maze is:")
    for i in ver1: print(i)
    print()

    return ver1
