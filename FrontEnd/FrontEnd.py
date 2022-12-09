from pygame import *
from maze_backend import maze_gen
from maze_backend import maze_path

ans = maze_gen.make_maze(15, 8)

int()

interface = display.set_mode((1500, 850))
display.set_caption("Maze-Craze")
logo = image.load("maze.png")
display.set_icon(logo)
start = image.load("start.png")
way = image.load("way.png")
wall = image.load("wall.png")
exit = image.load("exit.png")
bg = image.load("interface.jpg")
bg = transform.scale(bg, (1500, 850)).convert_alpha()
pathimg = image.load("path.png")

playerimg = image.load("player.png")


def maze(Binary_code):
    y = 80
    for l in Binary_code:
        for i in range(len(l)):
            x = (45 * i)
            if l[i] == 0:
                interface.blit(way, (x + 150, y))
            elif l[i] == 1:
                interface.blit(wall, (x + 150, y))
            elif l[i] == 2:
                interface.blit(start, (x + 150, y))
                interface.blit(playerimg, (x + 150, y + 5))
            elif l[i] == 3:
                interface.blit(exit, (x + 150, y))
            elif l[i] == 4:
                interface.blit(pathimg, (x + 150, y))

        y += 45

playing = True
while playing:
    for i in event.get():
        if i.type == QUIT:
            playing = False
        interface.fill((255, 255, 255))
        interface.blit(bg, (0, 0))
        maze(ans)
        display.update()

if __name__ == '__main__':
    pass
