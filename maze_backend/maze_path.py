"""
We can find the shortest path between any two given points in a maze,
by dijkstra's algorithm.
The path function will return all the co-orditanes for the shortest path,
by using the make_step function used in maze_end_point file.

"""
from maze_backend import maze_end_Point

def path(mazelist,end,start = (0,0)):

    """
    This fuction finds all the co-ordinates from the starting point and 
    and the ending point.
    """

    m = []
    for i in range(len(mazelist)):
        m.append([])
        for j in range(len(mazelist[i])):
            m[-1].append(0)
    i,j = start
    m[i][j] = 1
    
    k = 0
    chk, max_cord = True, 0
    while m[end[0]][end[1]] == 0:
        k += 1
        chk, max_cord = maze_end_Point.make_step(mazelist,k,m,max_cord)
    
    i, j = end[0],end[1]
    k = m[i][j]
    the_path = [(i,j)]
    while k > 1:
      if i > 0 and m[i - 1][j] == k-1:
        i, j = i-1, j
        the_path.append((i, j))
        k-=1
      elif j > 0 and m[i][j - 1] == k-1:
        i, j = i, j-1
        the_path.append((i, j))
        k-=1
      elif i < len(m) - 1 and m[i + 1][j] == k-1:
        i, j = i+1, j
        the_path.append((i, j))
        k-=1
      elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
        i, j = i, j+1
        the_path.append((i, j))
        k -= 1

    print("The co-ordinates for the shortest path for the given start and end points are:\n", the_path)
    return the_path


# #Uncomment to test
# mazelist = [[0, 0, 0, 0, 0],[0, 1, 1, 1, 1],[0, 0, 0, 0, 0],[1, 1, 1, 1, 0],[0, 1, 0, 0, 0],[0, 1, 0, 1, 0],[0, 0, 0, 1, 0]]
# start = 0, 0 #U can change the start point by giving different co-ordinates
# end = 4,0
# path(mazelist, end, start) #U can change the start and end points by giving different co-ordinates
