"""
We can find the shortest path between any two given points in a maze,
by dijkstra's algorithm.
The path function will return all the co-orditanes for the shortest path,
by using the make_step function used in maze_end_point file.

"""
from maze_backend import maze_end_Point

def path(mazelist,start = (0,0)):

    """
    This fuction finds all the co-ordinates from the starting point and 
    and the ending point.
    """

    def Initialisation(mazelist):
      mazelist[0][0] = 0
      for i in range(len(mazelist)):
        for j in range(len(mazelist[0])):
          if mazelist[i][j] == 3: 
            mazelist[i][j] = 0
            end = i,j
            return mazelist, end

    mazelist, end = Initialisation(mazelist)

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

    for i in the_path:
      mazelist[i[0]][i[1]] = 4
    mazelist[end[0]][end[1]] = 3
    mazelist[start[0]][start[1]] = 2

    print("The solution maze is:")
    for i in mazelist: print(i)
    
    return mazelist
