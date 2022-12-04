from maze_backend import maze_gen
from maze_backend import maze_path
from maze_backend import maze_end_Point

w, h = 3, 4

#values of w and h can be changed
mazelist = maze_gen.make_maze(w , h)

start = 0, 0

#U can change the start point by giving different co-ordinates
end = maze_end_Point.find_end(mazelist,start) 

#U can change the start and end points by giving different co-ordinates
maze_path.path(mazelist, end, start)
