from pygame import *
from maze_backend import maze_gen
from maze_backend import maze_path


mcode = maze_gen.make_maze(5, 6)
Binary_code = mcode

int()

interface = display.set_mode((700, 700))
display.set_caption("Maze-Craze")
logo = image.load("maze.png")
display.set_icon(logo)
start = image.load("start.png")
way = image.load("way.png")
wall = image.load("wall.png")
exit = image.load("exit.png")
bg = image.load("interface.jpg")
bg = transform.scale(bg, (700, 700)).convert_alpha()


def maze(Binary_code):
    y = 120
    for l in Binary_code:
        for i in range(len(l)):
            x = (45 * i)
            if l[i] == 0:
                interface.blit(way, (x + 120, y))

            elif l[i] == 1:
                interface.blit(wall, (x + 120, y))
            elif l[i] == 3:
                interface.blit(exit, (x + 120, y))
            else:
                interface.blit(start, (x + 120, y))

        y += 45



playing = True
while playing:
    for i in event.get():
        if i.type == QUIT:
            playing = False
        interface.fill((255, 255, 255))
        interface.blit(bg, (0, 0))
        maze(Binary_code)
        display.update()

if __name__ == '__main__':
    pass
